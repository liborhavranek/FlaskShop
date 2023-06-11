""" Libor Havránek App Copyright (C)  23.3 2023 """

from flask import Blueprint, render_template, request, flash, redirect
from flask_login import current_user

from myshop import db
from myshop.models.category_model import Category
from myshop.models.product_model import Product

admin = Blueprint("admin", __name__, template_folder="templates")


@admin.route("/")
def admin_page() -> str:
    return render_template("admin.html", customer=current_user)


@admin.route("/warehouse")
def warehouse():
    page = request.args.get("page", 1, type=int)
    per_page = 10  # Number of products per page

    category_id = request.args.get("category", type=int)
    query = Product.query
    if category_id:
        query = query.filter_by(category_id=category_id)

    products = query.order_by(Product.date_created.desc()).paginate(
        page=page, per_page=per_page
    )

    categories = Category.query.all()  # Fetch all categories

    return render_template(
        "admin/warehouse.html",
        customer=current_user,
        products=products,
        categories=categories,
        selected_category=category_id,
    )


@admin.route("/update_stock/<int:product_id>", methods=["POST"])
def update_stock(product_id):
    product = Product.query.get_or_404(product_id)
    stock_update = request.form.get("stock", type=int)

    if stock_update is not None:
        product.stock += stock_update
        db.session.commit()
        flash(f"Bylo naskladněno {stock_update} kusů{product.product_name}.", "success")
    else:
        flash("Invalid stock value.", "error")

    return redirect(request.referrer)
