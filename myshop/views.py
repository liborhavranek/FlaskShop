""" Libor Havránek App Copyright (C)  23.3 2023 """

from flask import Blueprint, render_template, request

from myshop import db
from myshop.models.category_model import Category
from myshop.models.product_model import Product

views = Blueprint('views', __name__, template_folder='templates/views')


@views.route('/')
def view() -> str:
    categories = db.session.query(Category.category_name.distinct()).all()
    products = Product.query.order_by(Product.date_created.desc()).all()
    newest_products = Product.query.order_by(Product.date_created.desc()).limit(4).all()
    most_visit_products = Product.query.order_by(Product.visit_count.desc()).limit(4).all()
    return render_template('views.html', categories=categories, products=products, newest_products=newest_products, most_visit_products=most_visit_products)


@views.route('/<string:category_name>')
def get_products_by_category(category_name):
    categories = db.session.query(Category.category_name.distinct()).all()
    # that line code show only categories what have product
    # categories = db.session.query(Category.category_name.distinct()).join(Product).all()
    category = Category.query.filter_by(category_name=category_name).first_or_404()
    products = Product.query.filter_by(category_id=category.id).order_by(Product.date_created.desc()).all()
    return render_template('views_categories_products.html', products=products, category=category, categories=categories)
