""" Libor Havránek App Copyright (C)  23.3 2023 """

from flask import Blueprint, render_template

from myshop import db
from myshop.models.category_model import Category
from myshop.models.product_model import Product

views = Blueprint('views', __name__, template_folder='templates')


@views.route('/')
def view() -> str:
    categories = db.session.query(Category.category_name.distinct()).all()
    products = Product.query.order_by(Product.date_created.desc()).all()
    newest_products = Product.query.order_by(Product.date_created.desc()).limit(5).all()
    return render_template('views.html', categories=categories, products=products, newest_products=newest_products)

