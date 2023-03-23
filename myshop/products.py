""" Libor Havránek App Copyright (C)  23.3 2023 """

from flask import Blueprint, render_template

products = Blueprint('products', __name__, template_folder='templates/products')


@products.route('/')
def product() -> str:
    return render_template('products.html')
