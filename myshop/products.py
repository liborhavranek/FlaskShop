""" Libor Havránek App Copyright (C)  23.3 2023 """

import os
import uuid

from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from flask_login import login_required
from datetime import datetime

from werkzeug.utils import secure_filename

from myshop import db
from myshop.forms.add_mobile_form import MobileForm
from myshop.forms.brand_form import BrandForm
from myshop.forms.category_form import CategoryForm
from myshop.forms.edit_all_product_image import AddProductAdditionalImagesForm
from myshop.forms.edit_product_image import EditProductMainImageForm
from myshop.models.brand_model import Brand
from myshop.models.category_model import Category
from myshop.models.images_model import ProductImage
from myshop.models.mobile_model import Mobile
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


def save_image(image, upload_folder):
    if image and image.filename != '':
        # Generate a unique filename for the image
        pic_filename = secure_filename(image.filename)
        pic_name = str(uuid.uuid1()) + "_" + pic_filename
        str_picname = str(pic_name)
        # Save the image file to the server
        image.save(os.path.join(upload_folder, str_picname))
        return str_picname
    return None


@products.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404


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
    brand = Brand.query.filter_by(id=id).first_or_404()
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
    brand = Brand.query.filter_by(id=id).first_or_404()
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
    category = Category.query.filter_by(id=id).first_or_404()
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
    category = Category.query.filter_by(id=id).first_or_404()
    db.session.delete(category)
    db.session.commit()
    flash('Kategorie byla smazána.', category='success')
    return redirect('/products/create-category')


@products.route('/product-preview/<int:product_id>')
def product_page_preview(product_id):
    product = Mobile.query.get(product_id)
    product.visit_count += 1
    db.session.commit()

    return render_template('product_page.html', product=product)


@products.route('/check-product', methods=['POST'])
def check_product():
    product_name = request.form['product_name']
    product = Product.query.filter_by(product_name=product_name).first()
    if product:
        return 'taken'
    else:
        return 'available'


@products.route('/products-list')
def product_list():
    products = Product.query.order_by(Product.date_created.desc()).all()
    return render_template('product-list.html', products=products)


@products.route('/edit-product-images/<int:product_id>', methods=['POST', 'GET'])
def edit_product_images(product_id):
    main_image_form = EditProductMainImageForm()
    additional_images_form = AddProductAdditionalImagesForm()
    product = Product.query.get_or_404(product_id)
    existing_image_filename = product.product_image

    if main_image_form.validate_on_submit():
        product_image = main_image_form.product_image.data
        if product_image:
            # Delete the existing image file
            if existing_image_filename:
                os.remove(os.path.join(current_app.config['UPLOAD_FOLDER'], existing_image_filename))
            # Save the new image file to the server
            new_image_filename = save_image(product_image, current_app.config['UPLOAD_FOLDER'])
            # Update the product image filename in the database
            product.product_image = new_image_filename
            db.session.commit()
            flash('Produktová fotka byla aktualizována.', category='success')
            return redirect(url_for('products.edit_product_images', product_id=product_id))

    if additional_images_form.validate_on_submit():
        additional_images = additional_images_form.additional_images.data
        additional_image_filenames = []
        for additional_image in additional_images:
            if additional_image.filename != '':
                # Save the additional image file to the server
                new_image_filename = save_image(additional_image, current_app.config['UPLOAD_FOLDER'])
                additional_image_filenames.append(new_image_filename)

        for filename in additional_image_filenames:
            product_image = ProductImage(
                image_name=filename,
                product_id=product_id
            )
            db.session.add(product_image)
        db.session.commit()

        flash('Další fotky byly přidány.', category='success')
        return redirect(url_for('products.edit_product_images', product_id=product_id))

    return render_template('edit_product_images.html', product=product, main_image_form=main_image_form,
                           additional_images_form=additional_images_form)


@products.route('/delete-product-image/<int:image_id>', methods=['GET', 'POST'])
@login_required
def delete_product_image(image_id):
    image = ProductImage.query.filter_by(id=image_id).first()
    if not image:
        flash('Fotka neexistuje.', category='error')
        return redirect(url_for('products.edit_product_images', product_id=image.product_id))
    try:
        os.remove(os.path.join(current_app.config['UPLOAD_FOLDER'], image.image_name))
    except OSError as e:
        flash(f'Nepodařilo se smazat fotku: {e}', category='error')
        return redirect(url_for('products.edit_product_images', product_id=image.product_id))
    db.session.delete(image)
    db.session.commit()
    flash('Fotka byla smazána.', category='success')
    return redirect(url_for('products.edit_product_images', product_id=image.product_id))


@products.route('/create-mobile-product', methods=['GET', 'POST'])
@login_required
def create_mobile_product():
    form = MobileForm()
    if form.validate_on_submit():
        product_data = {
            'product_name': request.form.get('product_name'),
            'price': request.form.get('price'),
            'discount': request.form.get('discount'),
            'stock': request.form.get('stock'),
            'sold': request.form.get('sold'),

            'height': float(request.form.get('height')),
            'height_units': request.form.get('height_units'),
            'width': float(request.form.get('width')),
            'width_units': request.form.get('width_units'),
            'depth': float(request.form.get('depth')),
            'depth_units': request.form.get('depth_units'),
            'weight': float(request.form.get('weight')),
            'weight_units': request.form.get('weight_units'),
            'color': request.form.get('color'),
            'subheading': request.form.get('subheading'),
            'description': request.form.get('description'),

            'display_size': request.form.get('display_size'),
            'display_resolution': request.form.get('display_resolution'),
            'operating_system': request.form.get('operating_system'),
            'operating_memory': request.form.get('operating_memory'),
            'memory': request.form.get('memory'),

            'battery_capacity': request.form.get('battery_capacity'),
            'memory_card_slot': request.form.get('memory_card_slot', type=bool),
            'face_id': request.form.get('face_id', type=bool),
            'touch_screen': request.form.get('touch_screen', type=bool),
            'back_camera': request.form.get('back_camera'),
            'front_camera': request.form.get('front_camera'),
            'convertible': request.form.get('convertible', type=bool),
            'wifi': request.form.get('wifi', type=bool),
            'bluetooth': request.form.get('bluetooth', type=bool),
            'nfc': request.form.get('nfc', type=bool),
            'esim': request.form.get('esim', type=bool),
            'processor': request.form.get('processor'),
            'processor_cores': request.form.get('processor_cores'),
            'brand_id': int(request.form.get('brand_id')),
            'category_id': int(request.form.get('category_id')),
            }

        # Get the product image file, if any
        product_image = request.files.get('product_image')
        product_data['product_image'] = save_image(product_image, current_app.config['UPLOAD_FOLDER'])

        new_product = Mobile(**product_data)

        # Get the additional image files, if any
        additional_images = request.files.getlist('additional_images')
        additional_image_filenames = [save_image(image, current_app.config['UPLOAD_FOLDER']) for image in
                                      additional_images if image.filename != '']

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

    return render_template('add_mobile_product.html', form=form)


@products.route('/edit-mobile-product/<int:product_id>', methods=['POST', 'GET'])
def edit_product(product_id):
    product = Mobile.query.get(product_id)
    form = MobileForm(obj=product)

    if request.method == 'POST':
        new_product_name = request.form.get('product_name')
        new_product_price = request.form.get('price')
        new_product_discount = request.form.get('discount')

        new_product_height = request.form.get('height')
        new_product_height_units = request.form.get('height_units')
        new_product_width = request.form.get('width')
        new_product_width_units = request.form.get('width_units')
        new_product_depth = request.form.get('depth')
        new_product_depth_units = request.form.get('depth_units')
        new_product_weight = request.form.get('weight')
        new_product_weight_units = request.form.get('weight_units')

        new_product_color = request.form.get('color')

        new_product_subheading = request.form.get('subheading')
        new_product_description = request.form.get('description')

        new_product_display_size = request.form.get('display_size')
        new_product_display_resolution = request.form.get('display_resolution')
        new_product_operating_system = request.form.get('operating_system')
        new_product_operating_memory = request.form.get('operating_memory')
        new_product_memory = request.form.get('memory')

        new_product_battery_capacity = request.form.get('battery_capacity')
        new_product_memory_card_slot = request.form.get('memory_card_slot')
        new_product_face_id = request.form.get('face_id')
        new_product_touch_screen = request.form.get('touch_screen')
        new_product_back_camera = request.form.get('back_camera')
        new_product_front_camera = request.form.get('front_camera')
        new_product_convertible = request.form.get('convertible')
        new_product_wifi = request.form.get('wifi')
        new_product_bluetooth = request.form.get('bluetooth')
        new_product_nfc = request.form.get('nfc')
        new_product_esim = request.form.get('esim')
        new_product_processor = request.form.get('processor')
        new_product_processor_cores = request.form.get('processor_cores')

        if new_product_name == str(product.id):
            # product name is the same as product id, so skip validation
            form.product_name.data = product.id
        else:
            # check if another product with the same name already exists
            existing_product = Product.query.filter_by(product_name=new_product_name).first()
            if existing_product and existing_product.id != product.id:
                # another product with the same name exists, so validation fails
                flash('Produkt s tímto názvem již existuje.', category='error')
            else:
                # no other product with the same name exists, so update the product name
                product.product_name = new_product_name
                product.price = new_product_price
                product.discount = new_product_discount

                product.height = new_product_height
                product.height_units = new_product_height_units
                product.width = new_product_width
                product.width_units = new_product_width_units
                product.depth = new_product_depth
                product.depth_units = new_product_depth_units
                product.weight = new_product_weight
                product.weight_units = new_product_weight_units

                product.color = new_product_color

                product.subheading = new_product_subheading
                product.description = new_product_description

                product.display_size = new_product_display_size
                product.display_resolution = new_product_display_resolution
                product.operating_system = new_product_operating_system
                product.operating_memory = new_product_operating_memory
                product.memory = new_product_memory

                product.battery_capacity = new_product_battery_capacity
                product.memory_card_slot = new_product_memory_card_slot == 'y'
                product.face_id = new_product_face_id == 'y'
                product.touch_screen = new_product_touch_screen == 'y'
                product.back_camera = new_product_back_camera
                product.front_camera = new_product_front_camera
                product.convertible = new_product_convertible == 'y'
                product.wifi = new_product_wifi == 'y'
                product.bluetooth = new_product_bluetooth == 'y'
                product.nfc = new_product_nfc == 'y'
                product.esim = new_product_esim == 'y'

                product.processor = new_product_processor
                product.processor_cores = new_product_processor_cores

                product.date_edited = datetime.utcnow()
                product.edited = True
                db.session.commit()
                form.product_name.data = ''
                flash('Produkt byl aktualizován.', category='success')
                return redirect(url_for('products.product_page_preview', product_id=product.id))

    return render_template('edit_mobile_product.html', product=product, form=form)


@products.route('/delete-mobile-product/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_mobile_product(id):
    product = Product.query.filter_by(id=id).first_or_404()
    product_images = ProductImage.query.filter_by(product_id=product.id).all()
    main_image = os.path.join(current_app.config['UPLOAD_FOLDER'], product.product_image)
    os.remove(main_image)
    for image in product_images:
        image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], image.image_name)
        os.remove(image_path)
        db.session.delete(image)
    db.session.delete(product)
    db.session.commit()
    flash('Produkt byl smazán.', category='success')
    return redirect('/products/products-list')
