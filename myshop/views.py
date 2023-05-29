""" Libor Havránek App Copyright (C)  23.3 2023 """

from flask import Blueprint, render_template, request, session, redirect, url_for
from flask_login import current_user

from myshop import db
from myshop.models.brand_model import Brand
from myshop.models.category_model import Category
from myshop.models.mobile_model import Mobile
from myshop.models.notebook_model import Notebook
from myshop.models.product_model import Product

views = Blueprint('views', __name__, template_folder='templates/views')


def sorting_category(category_name):
    if category_name == 'Mobily':
        brands = Brand.query.join(Mobile).filter(Mobile.brand_id == Brand.id).order_by(Brand.brand_name).distinct().all()
    elif category_name == 'Notebooky':
        brands = Brand.query.join(Notebook).filter(Notebook.brand_id == Brand.id).order_by(Brand.brand_name).distinct().all()
    else:
        brands = Brand.query.order_by(Brand.brand_name).distinct().all()
    return brands


def sort_products(products_query, sort_by):
    if sort_by == 'price_low':
        return products_query.order_by(Product.price)
    elif sort_by == 'price_high':
        return products_query.order_by(Product.price.desc())
    elif sort_by == 'most_views':
        return products_query.order_by(Product.visit_count.desc())
    elif sort_by == 'highest_discount':
        return products_query.order_by(Product.discount.desc())
    else:
        return products_query


@views.route('/')
def view() -> str:
    categories = db.session.query(Category.category_name.distinct()).all()
    products = Product.query.order_by(Product.date_created.desc()).all()
    newest_products = Product.query.order_by(Product.date_created.desc()).limit(4).all()
    most_visit_products = Product.query.order_by(Product.visit_count.desc()).limit(4).all()
    return render_template('views.html', categories=categories, products=products, newest_products=newest_products,
                           most_visit_products=most_visit_products, customer=current_user)


@views.route('/<string:category_name>/<string:brand_name>')
def get_products_by_category_and_brand(category_name, brand_name):
    categories = db.session.query(Category.category_name.distinct()).all()
    category = Category.query.filter_by(category_name=category_name).first_or_404()
    brand = Brand.query.filter_by(brand_name=brand_name).first_or_404()
    brands = sorting_category(category_name)

    # Get sorting option from query parameters
    sort_by = request.args.get('sort_by')

    products_query = Product.query.filter_by(category_id=category.id, brand_id=brand.id)
    sorted_products_query = sort_products(products_query, sort_by)
    products = sorted_products_query.all()

    return render_template('views_categories_products.html', products=products, category=category, brand=brand,
                           categories=categories, brands=brands, customer=current_user)


@views.route('/category/<string:category_name>')
def get_products_by_category(category_name):
    categories = db.session.query(Category.category_name.distinct()).all()
    category = Category.query.filter_by(category_name=category_name).first_or_404()
    brands = sorting_category(category_name)

    # Get sorting option from query parameters
    sort_by = request.args.get('sort_by')

    products_query = Product.query.filter_by(category_id=category.id)
    sorted_products_query = sort_products(products_query, sort_by)
    products = sorted_products_query.all()

    return render_template('views_categories_products.html', products=products, category=category,
                           categories=categories, brands=brands, customer=current_user)


@views.route('/search', methods=['GET', 'POST'])
def search_products():
    categories = db.session.query(Category.category_name.distinct()).all()
    query = request.args.get('query')  # Get the search query from the URL parameters

    if query:
        # Perform the search query
        products = Product.query.filter(Product.product_name.ilike(f"%{query}%")).all()
    else:
        # If no query is provided, display all products
        products = Product.query.all()

    return render_template('search_results.html', products=products, query=query, categories=categories,
                           customer=current_user)


@views.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    # Retrieve the product based on the given ID
    product = get_product_by_id(product_id)

    if product:
        if 'cart' not in session:
            session['cart'] = []

        cart = session['cart']
        cart.append(product)
        session['cart'] = cart

    return redirect(url_for('views.cart'))


@views.route('/cart')
def cart():
    cart = session.get('cart', [])
    return render_template('cart.html', cart=cart, customer=current_user)


def get_product_by_id(product_id):
    product = Product.query.get(product_id)
    if product:
        product_dict = {
            'id': product.id,
            'name': product.product_name,
            'price': product.price,
            'quantity': product.stock,
            # Include other attributes as needed
        }
        return product_dict
    return None
