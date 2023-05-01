""" Libor Havránek App Copyright (C)  23.3 2023 """
import os
import uuid

from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from flask_login import login_required
from datetime import datetime

from werkzeug.utils import secure_filename

from myshop import db
from myshop.forms.brand_form import BrandForm
from myshop.forms.category_form import CategoryForm
from myshop.forms.product_form import ProductForm
from myshop.models.brand_model import Brand
from myshop.models.category_model import Category
from myshop.models.images_model import ProductImage
from myshop.models.product_model import Product

products = Blueprint('products', __name__, template_folder='templates/products')


@products.route('/')
def product() -> str:
    return render_template('products.html')


path = 'myshop/static/images/uploads'
# upload photo staff
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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


@products.route('/create-product', methods=['GET', 'POST'])
@login_required
def create_product():
    form = ProductForm()
    if form.validate_on_submit():
        product_data = {
            'product_name': request.form.get('product_name'),
            'price': request.form.get('price'),
            'discount': request.form.get('discount'),
            'stock': request.form.get('stock'),
            'size': float(request.form.get('size')),
            'size_units': request.form.get('size_units'),
            'weight': float(request.form.get('weight')),
            'weight_units': request.form.get('weight_units'),
            'color': request.form.get('color'),
            'subheading': request.form.get('subheading'),
            'description': request.form.get('description'),
            'brand_id': int(request.form.get('brand_id')),
            'category_id': int(request.form.get('category_id')),
            }

        # Get the product image file, if any
        product_image = request.files.get('product_image')
        if product_image:
            # Generate a unique filename for the image
            pic_filename = secure_filename(product_image.filename)
            pic_name = str(uuid.uuid1()) + "_" + pic_filename
            str_picname = str(pic_name)
            # Save the image file to the server
            product_image.save(os.path.join(
                current_app.config['UPLOAD_FOLDER'], str_picname))
            # Add the image filename to the product data
            product_data['product_image'] = str_picname

        new_product = Product(**product_data)

        # Get the additional image files, if any
        additional_images = request.files.getlist('additional_images')
        additional_image_filenames = []
        for additional_image in additional_images:
            if additional_image.filename != '':
                # Generate a unique filename for the image
                pic_filename = secure_filename(additional_image.filename)
                pic_name = str(uuid.uuid1()) + "_" + pic_filename
                str_picname = str(pic_name)
                # Save the image file to the server
                additional_image.save(os.path.join(
                    current_app.config['UPLOAD_FOLDER'], str_picname))
                # Add the image filename to the list
                additional_image_filenames.append(str_picname)

        # Add the product to the database
        db.session.add(new_product)
        db.session.commit()

        # Add the additional images to the database
        for filename in additional_image_filenames:
            product_image = ProductImage(
                image_name=filename,
                product_id=new_product.id
            )
            db.session.add(product_image)
        db.session.commit()

        flash('Produkt byl přidán.', category='success')
        return redirect(url_for('products.product_page_preview', product_id=new_product.id))

    return render_template('add_product.html', form=form)


@products.route('/product-preview/<int:product_id>')
def product_page_preview(product_id):
    product = Product.query.get(product_id)
    return render_template('product_page.html', product=product)
