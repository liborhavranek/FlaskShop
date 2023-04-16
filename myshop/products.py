""" Libor Havránek App Copyright (C)  23.3 2023 """

from flask import Blueprint, render_template, request, flash
from flask_login import login_required

from myshop import db
from myshop.forms.brand_form import BrandForm
from myshop.models.brand_model import Brand

products = Blueprint('products', __name__, template_folder='templates/products')


@products.route('/')
def product() -> str:
    return render_template('products.html')


@products.route('/create-brand', methods=['GET', 'POST'])
@login_required
def create_brand():
    brands = Brand.query.all()
    form = BrandForm()
    if form.validate_on_submit():
        brand_data = {
            'brand_name': request.form.get('brand_name'),
        }
        new_brand = Brand(**brand_data)
        db.session.add(new_brand)
        db.session.commit()
        brands = Brand.query.all()
        flash('Značka byla vytvořena.', category='success')
    return render_template('add_brand.html', form=form, brands=brands)


@products.route('/check-brand', methods=['POST'])
def check_email():
    brand_name = request.form['brand_name']
    brand = Brand.query.filter_by(brand_name=brand_name).first()
    if brand:
        return 'taken'
    else:
        return 'available'
