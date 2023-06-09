""" Libor Havránek App Copyright (C)  23.3 2023 """
from datetime import datetime

from flask import Blueprint, render_template, request, session, redirect, flash, url_for
from flask_login import current_user, login_required

import json
from myshop import db
from myshop.forms.customer_order_form import CustomerOrderForm
from myshop.models.brand_model import Brand
from myshop.models.category_model import Category
from myshop.models.console_model import Console
from myshop.models.customer_model import Customer
from myshop.models.mobile_model import Mobile
from myshop.models.notebook_model import Notebook
from myshop.models.order_model import CustomerOrder
from myshop.models.product_model import Product
from myshop.models.smart_watch_model import SmartWatch
from myshop.models.wish_list_model import Wishlist

views = Blueprint("views", __name__, template_folder="templates/views")


# mark for add code if add new product
def sorting_category(category_name):
    if category_name == "Mobily":
        brands = (
            Brand.query.join(Mobile)
            .filter(Mobile.brand_id == Brand.id)
            .order_by(Brand.brand_name)
            .distinct()
            .all()
        )
    elif category_name == "Notebooky":
        brands = (
            Brand.query.join(Notebook)
            .filter(Notebook.brand_id == Brand.id)
            .order_by(Brand.brand_name)
            .distinct()
            .all()
        )
    elif category_name == "Herní konzole":
        brands = (
            Brand.query.join(Console)
            .filter(Console.brand_id == Brand.id)
            .order_by(Brand.brand_name)
            .distinct()
            .all()
        )
    elif category_name == "Hodinky":
        brands = (
            Brand.query.join(SmartWatch)
            .filter(SmartWatch.brand_id == Brand.id)
            .order_by(Brand.brand_name)
            .distinct()
            .all()
        )
    else:
        brands = Brand.query.order_by(Brand.brand_name).distinct().all()
    return brands


def sort_products(products_query, sort_by):
    if sort_by == "price_low":
        return products_query.order_by(Product.price)
    elif sort_by == "price_high":
        return products_query.order_by(Product.price.desc())
    elif sort_by == "most_views":
        return products_query.order_by(Product.visit_count.desc())
    elif sort_by == "highest_discount":
        return products_query.order_by(Product.discount.desc())
    else:
        return products_query


@views.route("/")
def view() -> str:
    categories = db.session.query(Category.category_name.distinct()).all()
    products = Product.query.order_by(Product.date_created.desc()).all()
    newest_products = Product.query.order_by(Product.date_created.desc()).limit(8).all()
    most_visit_products = (
        Product.query.order_by(Product.visit_count.desc()).limit(8).all()
    )
    most_selling_products = Product.query.order_by(Product.sold.desc()).limit(8).all()
    return render_template(
        "views.html",
        categories=categories,
        products=products,
        newest_products=newest_products,
        most_visit_products=most_visit_products,
        customer=current_user,
        most_selling_products=most_selling_products,
    )


@views.route("/<string:category_name>/<string:brand_name>")
def get_products_by_category_and_brand(category_name, brand_name):
    categories = db.session.query(Category.category_name.distinct()).all()
    category = Category.query.filter_by(category_name=category_name).first_or_404()
    brand = Brand.query.filter_by(brand_name=brand_name).first_or_404()
    brands = sorting_category(category_name)

    # Get sorting option from query parameters
    sort_by = request.args.get("sort_by")

    products_query = Product.query.filter_by(category_id=category.id, brand_id=brand.id)
    sorted_products_query = sort_products(products_query, sort_by)
    products = sorted_products_query.all()

    return render_template(
        "views_categories_products.html",
        products=products,
        category=category,
        brand=brand,
        categories=categories,
        brands=brands,
        customer=current_user,
    )


@views.route("/category/<string:category_name>")
def get_products_by_category(category_name):
    categories = db.session.query(Category.category_name.distinct()).all()
    category = Category.query.filter_by(category_name=category_name).first_or_404()
    brands = sorting_category(category_name)

    # Get sorting option from query parameters
    sort_by = request.args.get("sort_by")

    products_query = Product.query.filter_by(category_id=category.id)
    sorted_products_query = sort_products(products_query, sort_by)
    products = sorted_products_query.all()

    return render_template(
        "views_categories_products.html",
        products=products,
        category=category,
        categories=categories,
        brands=brands,
        customer=current_user,
    )


@views.route("/search", methods=["GET", "POST"])
def search_products():
    categories = db.session.query(Category.category_name.distinct()).all()
    query = request.args.get("query")  # Get the search query from the URL parameters

    if query:
        # Perform the search query
        products = Product.query.filter(Product.product_name.ilike(f"%{query}%")).all()
    else:
        # If no query is provided, display all products
        products = Product.query.all()

    return render_template(
        "search_results.html",
        products=products,
        query=query,
        categories=categories,
        customer=current_user,
    )


@views.route("/add_to_cart/<int:product_id>")
def add_to_cart(product_id):
    # Retrieve the product based on the given ID
    product = get_product_by_id(product_id)

    if product:
        if "cart" not in session:
            session["cart"] = []

        cart = session["cart"]

        # Check if the product is already in the cart
        for item in cart:
            if item["id"] == product_id:
                # Check if adding another quantity exceeds the stock
                if item["quantity"] >= product["stock"]:
                    flash("Více produktů už není na skladě", "error")
                    return redirect(request.referrer)

                # Increase the quantity of the existing product in the cart
                item["quantity"] += 1
                session["cart"] = cart
                flash("Produkt byl přidán do košíku", "success")
                return redirect(request.referrer)

        # Check if the product is in stock
        if product["stock"] <= 0:
            flash("Produkt již není na skaldě", "error")
            return redirect(request.referrer)

        # Add the product to the cart with quantity = 1
        product["quantity"] = 1
        cart.append(product)
        session["cart"] = cart
        flash("Produkt byl přidán do košíku", "success")

    return redirect(request.referrer)


@views.route("/cart")
def cart():
    categories = db.session.query(Category.category_name.distinct()).all()
    cart = session.get("cart", [])
    total_price = 0
    discounted_price = 0

    for item in cart:
        if item["discount"] == 0:
            total_price += item["price"] * item["quantity"]
        else:
            discounted_price += (
                item["price"] * item["quantity"] * (100 - item["discount"]) / 100
            )

    price_without_tax = round((total_price + discounted_price) * 0.79, 1)
    total_price = round(price_without_tax / 0.79, 1)
    tax = round(total_price * 0.21, 1)

    return render_template(
        "cart.html",
        cart=cart,
        customer=current_user,
        categories=categories,
        total_price=total_price,
        price_without_tax=price_without_tax,
        tax=tax,
        discounted_price=discounted_price,
    )


def get_product_by_id(product_id):
    product = Product.query.get(product_id)
    if product:
        product_dict = {
            "id": product.id,
            "product_name": product.product_name,
            "price": int(product.price),
            "stock": product.stock,
            "discount": product.discount
            # Include other attributes as needed
        }
        return product_dict
    return None


@views.route("/delete_from_cart/<int:product_id>")
def delete_from_cart(product_id):
    cart = session.get("cart", [])
    for item in cart:
        if item["id"] == product_id:
            cart.remove(item)
            session["cart"] = cart
            break

    return redirect(request.referrer)


@views.route("/withdraw_from_cart/<int:product_id>")
def withdraw_from_cart(product_id):
    cart = session.get("cart", [])
    for item in cart:
        if item["id"] == product_id:
            if item["quantity"] > 1:
                item["quantity"] -= 1
            else:
                cart.remove(item)
            session["cart"] = cart
            flash("Produkt byl odebrán z košíku", "success")
            break

    return redirect(request.referrer)


@views.route("/delivery", methods=["GET", "POST"])
def delivery():
    categories = db.session.query(Category.category_name.distinct()).all()
    cart = session.get("cart", [])
    total_price = 0
    discounted_price = 0

    for item in cart:
        if item["discount"] == 0:
            total_price += item["price"] * item["quantity"]
        else:
            discounted_price += (
                item["price"] * item["quantity"] * (100 - item["discount"]) / 100
            )

    price_without_tax = round((total_price + discounted_price) * 0.79, 1)
    total_price = round(price_without_tax / 0.79, 1)
    tax = round(total_price * 0.21, 1)

    form = CustomerOrderForm(request.form)

    if form.validate_on_submit():
        # Create a new CustomerOrder instance
        order_data = {
            "customer_id": current_user.id if current_user.is_authenticated else None,
            "customer_first_name": request.form.get("customer_first_name"),
            "customer_last_name": request.form.get("customer_last_name"),
            "customer_email": request.form.get("customer_email"),
            "customer_phone_code": request.form.get("customer_phone_code"),
            "customer_phone": request.form.get("customer_phone"),
            "customer_city": request.form.get("customer_city"),
            "customer_street": request.form.get("customer_street"),
            "customer_zipcode": request.form.get("customer_zipcode"),
            "customer_info": request.form.get("customer_info"),
            "payment_status": False,  # Set the payment status as needed (False for pending)
            "order_date": datetime.utcnow(),
            "products": json.dumps(cart),  # Serialize products as JSON
            "total_price": total_price,
        }

        new_order = CustomerOrder(**order_data)

        # Update the product quantities and sold count
        for item in cart:
            product = Product.query.get(item["id"])
            if product:
                quantity = item["quantity"]
                if quantity <= product.stock:
                    product.stock -= quantity
                    product.sold += quantity

        # Save the order to the database
        db.session.add(new_order)
        db.session.commit()

        session.pop("cart", None)

        # Redirect or render a success page
        return redirect(url_for("views.payment", order_id=new_order.id))

    return render_template(
        "delivery.html",
        cart=cart,
        customer=current_user,
        categories=categories,
        total_price=total_price,
        price_without_tax=price_without_tax,
        tax=tax,
        form=form,
    )


@views.route("/payment/<int:order_id>", methods=["GET", "POST"])
def payment(order_id):
    categories = db.session.query(Category.category_name.distinct()).all()
    order = CustomerOrder.query.get_or_404(order_id)
    products = json.loads(order.products)  # Parse the JSON string into a Python object
    total_price = order.total_price
    price_without_tax = round(total_price * 0.79, 1)
    tax = round(total_price * 0.21, 1)

    if order.payment_status:
        # Redirect the user to a different page if the payment has already been completed
        return redirect(url_for("views.payment_completed", order_id=order.id))

    if request.method == "POST":
        order.payment_status = True  # Set payment_status to True
        db.session.commit()
        # Perform payment processing or any other necessary actions here
        return redirect(url_for("views.thanks_for_buy"))

    return render_template(
        "payment.html",
        customer=current_user,
        products=products,
        order=order,
        categories=categories,
        price_without_tax=price_without_tax,
        tax=tax,
    )


@views.route("/thanks-for-buy")
def thanks_for_buy():
    categories = db.session.query(Category.category_name.distinct()).all()
    return render_template(
        "thanks_for_buy.html", categories=categories, customer=current_user
    )


@views.route("/payment-completed/<int:order_id>")
def payment_completed(order_id):
    categories = db.session.query(Category.category_name.distinct()).all()
    order = CustomerOrder.query.get_or_404(order_id)
    products = json.loads(order.products)  # Parse the JSON string into a Python object
    total_price = order.total_price
    price_without_tax = round(total_price * 0.79, 1)
    tax = round(total_price * 0.21, 1)
    return render_template(
        "payment_complete.html",
        categories=categories,
        customer=current_user,
        products=products,
        order=order,
        price_without_tax=price_without_tax,
        tax=tax,
    )


@views.route("/orders/<int:customer_id>")
def orders(customer_id):
    categories = db.session.query(Category.category_name.distinct()).all()
    customer = Customer.query.get_or_404(customer_id)
    orders = CustomerOrder.query.filter_by(customer_id=customer_id).all()

    return render_template(
        "customer_orders.html", customer=customer, orders=orders, categories=categories
    )


@views.route("/toggle_wishlist/<int:product_id>", methods=["POST"])
@login_required
def toggle_wishlist(product_id):
    # Retrieve the product object
    product = Product.query.get(product_id)

    # Check if the product exists
    if product is None:
        flash("Product not found", "error")
        return redirect(request.referrer)

    # Get the current customer from the authenticated user
    customer = Customer.query.get(current_user.id)

    # Check if the customer exists
    if customer is None:
        flash("Customer not found", "error")
        return redirect(request.referrer)

    # Check if the product is already in the customer's wishlist
    wishlist_entry = Wishlist.query.filter_by(
        customer_id=customer.id, product_id=product.id
    ).first()
    if wishlist_entry:
        # Remove the product from the wishlist
        db.session.delete(wishlist_entry)
        flash("Product removed from wishlist", "info")
    else:
        # Add the product to the wishlist
        wishlist_entry = Wishlist(customer_id=customer.id, product_id=product.id)
        db.session.add(wishlist_entry)
        flash("Product added to wishlist", "success")

    db.session.commit()

    return redirect(request.referrer)


@views.route("/wishlist/<int:customer_id>")
@login_required
def wishlist(customer_id):
    categories = db.session.query(Category.category_name.distinct()).all()
    customer = Customer.query.get_or_404(customer_id)
    wishlist_products = customer.wishlist

    return render_template(
        "wishlist.html",
        categories=categories,
        customer=customer,
        wishlist_products=wishlist_products,
    )


@views.route("/wishlist/delete/<int:wishlist_id>", methods=["POST", "DELETE"])
@login_required
def delete_wishlist(wishlist_id):
    # Retrieve the wishlist entry
    wishlist_entry = Wishlist.query.get(wishlist_id)

    # Check if the wishlist entry exists
    if wishlist_entry is None:
        flash("Wishlist entry not found", "error")
        return redirect(request.referrer)

    # Check if the current user is the owner of the wishlist entry
    if wishlist_entry.customer_id != current_user.id:
        flash("You are not authorized to delete this wishlist entry", "error")
        return redirect(request.referrer)

    # Remove the wishlist entry from the database
    db.session.delete(wishlist_entry)
    db.session.commit()

    flash("Wishlist entry deleted", "info")
    return redirect(request.referrer)
