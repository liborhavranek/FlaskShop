""" Libor Havránek App Copyright (C)  23.3 2023 """


from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_required
from datetime import datetime
from myshop import db
from myshop.forms.brand_form import BrandForm
from myshop.forms.category_form import CategoryForm
from myshop.models.brand_model import Brand
from myshop.models.category_model import Category

products = Blueprint('products', __name__, template_folder='templates/products')


@products.route('/')
def product() -> str:
    return render_template('products.html')


@products.route('/create-brand', methods=['GET', 'POST'])
@login_required
def create_brand():
    brands = Brand.query.order_by(Brand.date_created.desc()).all()
    form = BrandForm()
    if form.validate_on_submit():
        brand_data = {
            'brand_name': request.form.get('brand_name'),
        }
        new_brand = Brand(**brand_data)
        db.session.add(new_brand)
        db.session.commit()
        form.brand_name.data = ''
        brands = Brand.query.order_by(Brand.date_created.desc()).all()
        flash('Značka byla vytvořena.', category='success')
    return render_template('add_brand.html', form=form, brands=brands)


@products.route('/check-brand', methods=['POST'])
def check_brand():
    brand_name = request.form['brand_name']
    brand = Brand.query.filter_by(brand_name=brand_name).first()
    if brand:
        return 'taken'
    else:
        return 'available'


@products.route('/edit-brand/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_brand(id):
    brand = Brand.query.filter_by(id=id).first()
    form = BrandForm()
    if form.validate_on_submit():
        brand.brand_name = request.form.get('brand_name')
        brand.date_edited = datetime.utcnow()  # Set the current time for date_edited
        brand.edited = True
        db.session.commit()
        form.brand_name.data = ''
        flash('Značka byla aktualizována.', category='success')
    return render_template('edit_brand.html', brand=brand, form=form)


@products.route('/delete-brand/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_brand(id):
    brand = Brand.query.filter_by(id=id).first()
    db.session.delete(brand)
    db.session.commit()
    flash('Značka byla smazána.', category='success')
    return redirect('/products/create-brand')


@products.route('/create-category', methods=['GET', 'POST'])
@login_required
def create_category():
    categories = Category.query.order_by(Category.date_created.desc()).all()
    form = CategoryForm()
    if form.validate_on_submit():
        category_data = {
            'category_name': request.form.get('category_name'),
        }
        new_category = Category(**category_data)
        db.session.add(new_category)
        db.session.commit()
        form.category_name.data = ''
        categories = Category.query.order_by(Category.date_created.desc()).all()
        flash('Kategorie byla vytvořena.', category='success')
    return render_template('add_category.html', form=form, categories=categories)


@products.route('/edit-category/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_category(id):
    category = Category.query.filter_by(id=id).first()
    form = CategoryForm()
    if form.validate_on_submit():
        category.category_name = request.form.get('category_name')
        category.date_edited = datetime.utcnow()  # Set the current time for date_edited
        category.edited = True
        db.session.commit()
        form.category_name.data = ''
        flash('Značka byla aktualizována.', category='success')
    return render_template('edit_category.html', category=category, form=form)


@products.route('/check-category', methods=['POST'])
def check_category():
    category_name = request.form['category_name']
    category = Category.query.filter_by(category_name=category_name).first()
    if category:
        return 'taken'
    else:
        return 'available'

@products.route('/delete-category/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_category(id):
    category = Category.query.filter_by(id=id).first()
    db.session.delete(category)
    db.session.commit()
    flash('Kategorie byla smazána.', category='success')
    return redirect('/products/create-category')
