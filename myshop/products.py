""" Libor Havránek App Copyright (C)  23.3 2023 """

from flask import Blueprint, render_template

from myshop.forms.brand_form import BrandForm

products = Blueprint('products', __name__, template_folder='templates/products')


@products.route('/')
def product() -> str:
    return render_template('products.html')


@products.route('/create-brand')
def create_brand():
    form = BrandForm()
    return render_template('add_brand.html', form=form)
