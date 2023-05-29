""" Libor Havránek App Copyright (C)  23.3 2023 """

from flask import Blueprint, render_template, request

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


@views.route('/')
def view() -> str:
    categories = db.session.query(Category.category_name.distinct()).all()
    products = Product.query.order_by(Product.date_created.desc()).all()
    newest_products = Product.query.order_by(Product.date_created.desc()).limit(4).all()
    most_visit_products = Product.query.order_by(Product.visit_count.desc()).limit(4).all()
    return render_template('views.html', categories=categories, products=products, newest_products=newest_products, most_visit_products=most_visit_products)


@views.route('/<string:category_name>/<string:brand_name>')
def get_products_by_category_and_brand(category_name, brand_name):
    categories = db.session.query(Category.category_name.distinct()).all()
    category = Category.query.filter_by(category_name=category_name).first_or_404()
    brand = Brand.query.filter_by(brand_name=brand_name).first_or_404()
    brands = sorting_category(category_name)

    # Get sorting option from query parameters
    sort_by = request.args.get('sort_by')

    products_query = Product.query.filter_by(category_id=category.id, brand_id=brand.id)

    if sort_by == 'price_low':
        products_query = products_query.order_by(Product.price)
    elif sort_by == 'price_high':
        products_query = products_query.order_by(Product.price.desc())
    elif sort_by == 'most_views':
        products_query = products_query.order_by(Product.visit_count.desc())
    elif sort_by == 'highest_discount':
        products_query = products_query.order_by(Product.discount.desc())

    products = products_query.all()

    return render_template('views_categories_products.html', products=products, category=category, brand=brand, categories=categories, brands=brands)


@views.route('/category/<string:category_name>')
def get_products_by_category(category_name):
    categories = db.session.query(Category.category_name.distinct()).all()
    category = Category.query.filter_by(category_name=category_name).first_or_404()
    brands = sorting_category(category_name)

    # Get sorting option from query parameters
    sort_by = request.args.get('sort_by')

    products_query = Product.query.filter_by(category_id=category.id)

    if sort_by == 'price_low':
        products_query = products_query.order_by(Product.price)
    elif sort_by == 'price_high':
        products_query = products_query.order_by(Product.price.desc())
    elif sort_by == 'most_views':
        products_query = products_query.order_by(Product.visit_count.desc())
    elif sort_by == 'highest_discount':
        products_query = products_query.order_by(Product.discount.desc())

    products = products_query.all()

    return render_template('views_categories_products.html', products=products, category=category, categories=categories, brands=brands)
