""" Libor Havránek App Copyright (C)  23.3 2023 """

import os
import uuid

from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from flask_login import login_required, current_user
from datetime import datetime

from werkzeug.utils import secure_filename

from myshop import db
from myshop.forms.add_console_form import ConsoleForm
from myshop.forms.add_mobile_form import MobileForm
from myshop.forms.add_notebook_form import NotebookForm
from myshop.forms.add_smart_watch_form import SmartWatchForm
from myshop.forms.brand_form import BrandForm
from myshop.forms.category_form import CategoryForm
from myshop.forms.edit_all_product_image import AddProductAdditionalImagesForm
from myshop.forms.edit_product_image import EditProductMainImageForm
from myshop.models.brand_model import Brand
from myshop.models.category_model import Category
from myshop.models.console_model import Console
from myshop.models.images_model import ProductImage
from myshop.models.mobile_model import Mobile
from myshop.models.notebook_model import Notebook
from myshop.models.product_model import Product
from myshop.models.smart_watch_model import SmartWatch

products = Blueprint('products', __name__, template_folder='templates/products')


@products.route('/')
def product() -> str:
    return render_template('products.html', customer=current_user)


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
    return render_template('errors/404.html', customer=current_user), 404


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
    return render_template('add_brand.html', form=form, brands=brands, customer=current_user)


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
    return render_template('edit_brand.html', brand=brand, form=form, customer=current_user)


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
    return render_template('add_category.html', form=form, categories=categories, customer=current_user)


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
    return render_template('edit_category.html', category=category, form=form, customer=current_user)


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


# mark for add code if add new product
@products.route('/product-preview/<int:product_id>')
def product_page_preview(product_id):
    categories = db.session.query(Category.category_name.distinct()).all()
    product = Product.query.get(product_id)
    mobile = Mobile.query.get(product_id)
    notebook = Notebook.query.get(product_id)
    console = Console.query.get(product_id)
    smart_watch = SmartWatch.query.get(product_id)
    product.visit_count += 1
    db.session.commit()

    discount_price = product.price - (product.price * product.discount / 100)
    discount = product.price - discount_price

    if isinstance(mobile, Product):
        return render_template('mobile_product_page.html', product=mobile, customer=current_user,
                               categories=categories, discount_price=discount_price, discount=discount)
    elif isinstance(notebook, Product):
        return render_template('notebook_product_page.html', product=notebook, customer=current_user,
                               categories=categories, discount_price=discount_price, discount=discount,
                               notebook=notebook)
    elif isinstance(console, Product):
        return render_template('console_product_page.html', product=console, customer=current_user,
                               categories=categories, discount_price=discount_price, discount=discount)
    elif isinstance(smart_watch, Product):
        return render_template('smart_watch_product_page.html', product=smart_watch, customer=current_user,
                               categories=categories, discount_price=discount_price, discount=discount)


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
    return render_template('product-list.html', products=products, customer=current_user)


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
            return redirect(url_for('products.edit_product_images', product_id=product_id, customer=current_user))

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
        return redirect(url_for('products.edit_product_images', product_id=product_id, customer=current_user))

    return render_template('edit_product_images.html', product=product, main_image_form=main_image_form,
                           additional_images_form=additional_images_form, customer=current_user)


@products.route('/delete-product-image/<int:image_id>', methods=['GET', 'POST'])
@login_required
def delete_product_image(image_id):
    image = ProductImage.query.filter_by(id=image_id).first()
    if not image:
        flash('Fotka neexistuje.', category='error')
        return redirect(url_for('products.edit_product_images', product_id=image.product_id, customer=current_user))
    try:
        os.remove(os.path.join(current_app.config['UPLOAD_FOLDER'], image.image_name))
    except OSError as e:
        flash(f'Nepodařilo se smazat fotku: {e}', category='error')
        return redirect(url_for('products.edit_product_images', product_id=image.product_id, customer=current_user))
    db.session.delete(image)
    db.session.commit()
    flash('Fotka byla smazána.', category='success')
    return redirect(url_for('products.edit_product_images', product_id=image.product_id, customer=current_user))


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

            'product_type': "Mobile",

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
        return redirect(url_for('products.product_page_preview', product_id=new_product.id, customer=current_user))

    return render_template('add_mobile_product.html', form=form, customer=current_user)


@products.route('/edit-mobile-product/<int:product_id>', methods=['POST', 'GET'])
@login_required
def edit_product(product_id):
    product = Mobile.query.get(product_id)
    form = MobileForm(obj=product)

    if request.method == 'POST':
        new_product_name = request.form.get('product_name')
        new_product_price = request.form.get('price')
        new_product_discount = request.form.get('discount')

        new_product_brand = request.form.get('brand_id')
        new_product_category = request.form.get('category_id')

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

                product.brand_id = new_product_brand
                product.category_id = new_product_category

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
                return redirect(url_for('products.product_page_preview', product_id=product.id, customer=current_user))

    return render_template('edit_mobile_product.html', product=product, form=form, customer=current_user)


@products.route('/delete-mobile-product/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_mobile_product(id):
    product = Product.query.filter_by(id=id).first_or_404()
    mobile = Mobile.query.filter_by(id=id).first_or_404()

    product_images = ProductImage.query.filter_by(product_id=product.id).all()
    main_image = os.path.join(current_app.config['UPLOAD_FOLDER'], product.product_image)
    os.remove(main_image)
    for image in product_images:
        image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], image.image_name)
        os.remove(image_path)
        db.session.delete(image)
    db.session.delete(product)
    db.session.delete(mobile)
    db.session.commit()
    flash('Produkt byl smazán.', category='success')
    return redirect('/products/products-list')


@products.route('/delete-notebook-product/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_notebook_product(id):
    product = Product.query.filter_by(id=id).first_or_404()
    notebook = Notebook.query.filter_by(id=id).first_or_404()

    product_images = ProductImage.query.filter_by(product_id=product.id).all()
    main_image = os.path.join(current_app.config['UPLOAD_FOLDER'], product.product_image)
    os.remove(main_image)
    for image in product_images:
        image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], image.image_name)
        os.remove(image_path)
        db.session.delete(image)
    db.session.delete(product)
    db.session.delete(notebook)
    db.session.commit()
    flash('Produkt byl smazán.', category='success')
    return redirect('/products/products-list')


@products.route('/create-notebook-product', methods=['GET', 'POST'])
@login_required
def create_notebook_product():
    form = NotebookForm()
    if form.validate_on_submit():
        product_data = {
            'product_name': request.form.get('product_name'),
            'price': request.form.get('price'),
            'discount': request.form.get('discount'),
            'stock': request.form.get('stock'),
            'sold': request.form.get('sold'),

            'subheading': request.form.get('subheading'),
            'description': request.form.get('description'),

            'product_type': "Notebook",

            'height': float(request.form.get('height')),
            'height_units': request.form.get('height_units'),
            'width': float(request.form.get('width')),
            'width_units': request.form.get('width_units'),
            'depth': float(request.form.get('depth')),
            'depth_units': request.form.get('depth_units'),
            'weight': float(request.form.get('weight')),
            'weight_units': request.form.get('weight_units'),
            'color': request.form.get('color'),


            'display_size': request.form.get('display_size'),
            'display_resolution': request.form.get('display_resolution'),
            'display_frequency': request.form.get('display_frequency'),
            'display_nits': request.form.get('display_nits'),
            'display_type': request.form.get('display_type'),

            'processor': request.form.get('processor'),
            'processor_cores': request.form.get('processor_cores'),

            'operating_memory': request.form.get('operating_memory'),

            'graphics_card': request.form.get('graphics_card'),
            'graphics_memory': request.form.get('graphics_memory'),

            'operating_system': request.form.get('operating_system'),

            'ssd': request.form.get('ssd', type=bool),
            'hdd': request.form.get('hdd', type=bool),
            'ssd_capacity': request.form.get('ssd_capacity'),
            'hdd_capacity': request.form.get('hdd_capacity'),

            'light_keyboard': request.form.get('light_keyboard', type=bool),
            'num_keyboard': request.form.get('num_keyboard', type=bool),
            'touch_screen': request.form.get('touch_screen', type=bool),
            'fingerprint_reader': request.form.get('fingerprint_reader', type=bool),
            'memory_card_reader': request.form.get('memory_card_reader', type=bool),
            'usb_c_charging': request.form.get('usb_c_charging', type=bool),


            'battery_capacity': request.form.get('battery_capacity'),
            'construction': request.form.get('construction'),

            'usb_ports': request.form.get('usb_ports', type=bool),
            'hdmi_ports': request.form.get('hdmi_ports', type=bool),
            'audio_jack': request.form.get('audio_jack', type=bool),
            'usb_3_0': request.form.get('usb_3_0', type=bool),
            'usb_2_0': request.form.get('usb_2_0', type=bool),
            'cd_dvd_drive': request.form.get('cd_dvd_drive', type=bool),

            'brand_id': int(request.form.get('brand_id')),
            'category_id': int(request.form.get('category_id')),
            }

        # Get the product image file, if any
        product_image = request.files.get('product_image')
        product_data['product_image'] = save_image(product_image, current_app.config['UPLOAD_FOLDER'])

        new_product = Notebook(**product_data)

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
        return redirect(url_for('products.product_page_preview', product_id=new_product.id, customer=current_user))
    return render_template('add_notebook_product.html', form=form, customer=current_user)


@login_required
@products.route('/edit-notebook-product/<int:product_id>', methods=['POST', 'GET'])
def edit_notebook_product(product_id):
    product = Notebook.query.get(product_id)
    form = NotebookForm(obj=product)

    if request.method == 'POST':
        new_product_name = request.form.get('product_name')

        new_product_subheading = request.form.get('subheading')
        new_product_description = request.form.get('description')

        new_product_color = request.form.get('color')
        new_product_brand = request.form.get('brand_id')
        new_product_category = request.form.get('category_id')

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

        new_product_display_size = request.form.get('display_size')
        new_product_display_resolution = request.form.get('display_resolution')
        new_product_display_frequency = request.form.get('display_frequency')
        new_product_display_nits = request.form.get('display_nits')
        new_product_display_type = request.form.get('display_type')

        new_product_processor = request.form.get('processor')
        new_product_processor_cores = request.form.get('processor_cores')

        new_product_operating_memory = request.form.get('operating_memory')
        new_product_graphics_card = request.form.get('graphics_card')
        new_product_graphics_memory = request.form.get('graphics_memory')

        new_product_operating_system = request.form.get('operating_system')

        new_product_battery_capacity = request.form.get('battery_capacity')
        new_product_construction = request.form.get('construction')
        new_product_usb_ports = request.form.get('usb_ports')
        new_product_hdmi_ports = request.form.get('hdmi_ports')

        new_product_hdd = request.form.get('hdd')
        new_product_ssd = request.form.get('ssd')
        new_product_hdd_capacity = request.form.get('hdd')
        new_product_ssd_capacity = request.form.get('ssd')

        new_product_light_keyboard = request.form.get('light_keyboard')
        new_product_num_keyboard = request.form.get('num_keyboard')
        new_product_touch_screen = request.form.get('touch_screen')
        new_product_fingerprint_reader = request.form.get('fingerprint_reader')
        new_product_memory_card_reader = request.form.get('memory_card_reader')
        new_product_usb_c_charging = request.form.get('usb_c_charging')

        new_product_audio_jack = request.form.get('audio_jack')
        new_product_usb_3_0 = request.form.get('usb_3_0')
        new_product_usb_2_0 = request.form.get('usb_2_0')
        new_product_cd_dvd_drive = request.form.get('cd_dvd_drive')


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

                product.subheading = new_product_subheading
                product.description = new_product_description

                product.color = new_product_color
                product.brand_id = new_product_brand
                product.category_id = new_product_category

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

                product.display_size = new_product_display_size
                product.display_resolution = new_product_display_resolution
                product.display_frequency = new_product_display_frequency
                product.display_nits = new_product_display_nits
                product.display_type = new_product_display_type

                product.processor = new_product_processor
                product.processor_cores = new_product_processor_cores

                product.operating_memory = new_product_operating_memory
                product.graphics_card = new_product_graphics_card
                product.graphics_memory = new_product_graphics_memory

                product.operating_system = new_product_operating_system
                product.battery_capacity = new_product_battery_capacity

                product.construction = new_product_construction
                product.usb_ports = new_product_usb_ports
                product.hdmi_ports = new_product_hdmi_ports

                product.hdd = new_product_hdd == 'y'
                product.ssd = new_product_ssd == 'y'
                product.hdd_capacity = new_product_hdd_capacity
                product.ssd_capacity = new_product_ssd_capacity

                product.light_keyboard = new_product_light_keyboard == 'y'
                product.num_keyboard = new_product_num_keyboard == 'y'
                product.touch_screen = new_product_touch_screen == 'y'
                product.fingerprint_reader = new_product_fingerprint_reader == 'y'
                product.memory_card_reader = new_product_memory_card_reader
                product.usb_c_charging = new_product_usb_c_charging == 'y'

                product.audio_jack = new_product_audio_jack == 'y'
                product.usb_3_0 = new_product_usb_3_0 == 'y'
                product.usb_2_0 = new_product_usb_2_0 == 'y'
                product.cd_dvd_drive = new_product_cd_dvd_drive == 'y'

                product.date_edited = datetime.utcnow()
                product.edited = True
                db.session.commit()
                form.product_name.data = ''
                flash('Produkt byl aktualizován.', category='success')
                return redirect(url_for('products.product_page_preview', product_id=product.id, customer=current_user))

    return render_template('edit_notebook_product.html', product=product, form=form, customer=current_user)


@products.route('/create-console-product', methods=['GET', 'POST'])
@login_required
def create_console_product():
    form = ConsoleForm()
    if form.validate_on_submit():
        product_data = {
            'product_name': request.form.get('product_name'),
            'price': request.form.get('price'),
            'discount': request.form.get('discount'),
            'stock': request.form.get('stock'),
            'sold': request.form.get('sold'),

            'product_type': "Console",

            'color': request.form.get('color'),
            'subheading': request.form.get('subheading'),
            'description': request.form.get('description'),

            'ssd': request.form.get('ssd', type=bool),
            'hdd': request.form.get('hdd', type=bool),
            'ssd_capacity': request.form.get('ssd_capacity'),
            'hdd_capacity': request.form.get('hdd_capacity'),

            'brand_id': int(request.form.get('brand_id')),
            'category_id': int(request.form.get('category_id')),
            }

        # Get the product image file, if any
        product_image = request.files.get('product_image')
        product_data['product_image'] = save_image(product_image, current_app.config['UPLOAD_FOLDER'])

        new_product = Console(**product_data)

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
        return redirect(url_for('products.product_page_preview', product_id=new_product.id, customer=current_user))

    return render_template('add_console_product.html', form=form, customer=current_user)


@login_required
@products.route('/edit-console-product/<int:product_id>', methods=['POST', 'GET'])
def edit_console_product(product_id):
    product = Console.query.get(product_id)
    form = ConsoleForm(obj=product)

    if request.method == 'POST':
        new_product_name = request.form.get('product_name')

        new_product_subheading = request.form.get('subheading')
        new_product_description = request.form.get('description')

        new_product_color = request.form.get('color')
        new_product_brand = request.form.get('brand_id')
        new_product_category = request.form.get('category_id')

        new_product_price = request.form.get('price')
        new_product_discount = request.form.get('discount')

        new_product_hdd = request.form.get('hdd')
        new_product_ssd = request.form.get('ssd')
        new_product_hdd_capacity = request.form.get('hdd')
        new_product_ssd_capacity = request.form.get('ssd')

        new_product_dvd_drive = request.form.get('dvd_drive')

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

                product.subheading = new_product_subheading
                product.description = new_product_description

                product.color = new_product_color
                product.brand_id = new_product_brand
                product.category_id = new_product_category

                product.price = new_product_price
                product.discount = new_product_discount

                product.hdd = new_product_hdd == 'y'
                product.ssd = new_product_ssd == 'y'
                product.hdd_capacity = new_product_hdd_capacity
                product.ssd_capacity = new_product_ssd_capacity

                product.dvd_drive = new_product_dvd_drive == 'y'

                product.date_edited = datetime.utcnow()
                product.edited = True
                db.session.commit()
                form.product_name.data = ''
                flash('Produkt byl aktualizován.', category='success')
                return redirect(url_for('products.product_page_preview', product_id=product.id, customer=current_user))

    return render_template('edit_console_product.html', product=product, form=form, customer=current_user)


@products.route('/delete-console-product/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_console_product(id):
    product = Product.query.filter_by(id=id).first_or_404()
    console = Console.query.filter_by(id=id).first_or_404()

    product_images = ProductImage.query.filter_by(product_id=product.id).all()
    main_image = os.path.join(current_app.config['UPLOAD_FOLDER'], product.product_image)
    os.remove(main_image)
    for image in product_images:
        image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], image.image_name)
        os.remove(image_path)
        db.session.delete(image)
    db.session.delete(product)
    db.session.delete(console)
    db.session.commit()
    flash('Produkt byl smazán.', category='success')
    return redirect('/products/products-list')


@products.route('/create-smart-watch-product', methods=['GET', 'POST'])
@login_required
def create_smart_watch_product():
    form = SmartWatchForm()
    if form.validate_on_submit():
        product_data = {
            'product_name': request.form.get('product_name'),
            'price': request.form.get('price'),
            'discount': request.form.get('discount'),
            'stock': request.form.get('stock'),
            'sold': request.form.get('sold'),

            'product_type': "Hodinky",

            'color': request.form.get('color'),
            'subheading': request.form.get('subheading'),
            'description': request.form.get('description'),

            'display_size': request.form.get('display_size'),
            'display_resolution': request.form.get('display_resolution'),


            'operating_system': request.form.get('operating_system'),
            'memory': request.form.get('memory'),
            'battery_capacity': request.form.get('battery_capacity'),

            'weight': float(request.form.get('weight')),
            'weight_units': request.form.get('weight_units'),

            'wifi': request.form.get('wifi', type=bool),
            'bluetooth': request.form.get('bluetooth', type=bool),
            'nfc': request.form.get('nfc', type=bool),
            'esim': request.form.get('esim', type=bool),

            'heart_rate_monitor': request.form.get('heart_rate_monitor', type=bool),
            'step_counter': request.form.get('step_counter', type=bool),
            'sleep_tracker': request.form.get('sleep_tracker', type=bool),
            'gps': request.form.get('gps', type=bool),
            'water_resistant': request.form.get('water_resistant', type=bool),
            'music_player': request.form.get('music_player', type=bool),
            'voice_assistant': request.form.get('voice_assistant', type=bool),

            'brand_id': int(request.form.get('brand_id')),
            'category_id': int(request.form.get('category_id')),
            }

        # Get the product image file, if any
        product_image = request.files.get('product_image')
        product_data['product_image'] = save_image(product_image, current_app.config['UPLOAD_FOLDER'])

        new_product = SmartWatch(**product_data)

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
        return redirect(url_for('products.product_page_preview', product_id=new_product.id, customer=current_user))

    return render_template('add_smart_watch_product.html', form=form, customer=current_user)


@products.route('/edit-smart-watch-product/<int:product_id>', methods=['POST', 'GET'])
@login_required
def edit_smart_watch_product(product_id):
    product = SmartWatch.query.get(product_id)
    form = SmartWatchForm(obj=product)

    if request.method == 'POST':
        new_product_name = request.form.get('product_name')
        new_product_price = request.form.get('price')
        new_product_discount = request.form.get('discount')

        new_product_brand = request.form.get('brand_id')
        new_product_category = request.form.get('category_id')

        new_product_weight = request.form.get('weight')
        new_product_weight_units = request.form.get('weight_units')

        new_product_color = request.form.get('color')

        new_product_subheading = request.form.get('subheading')
        new_product_description = request.form.get('description')

        new_product_display_size = request.form.get('display_size')
        new_product_display_resolution = request.form.get('display_resolution')
        new_product_operating_system = request.form.get('operating_system')
        new_product_memory = request.form.get('memory')

        new_product_battery_capacity = request.form.get('battery_capacity')

        new_product_wifi = request.form.get('wifi')
        new_product_bluetooth = request.form.get('bluetooth')
        new_product_nfc = request.form.get('nfc')
        new_product_esim = request.form.get('esim')

        new_product_heart_rate_monitor = request.form.get('heart_rate_monitor')
        new_product_step_counter = request.form.get('step_counter')
        new_product_sleep_tracker = request.form.get('sleep_tracker')
        new_product_gps = request.form.get('gps')
        new_product_water_resistant = request.form.get('water_resistant')
        new_product_music_player = request.form.get('music_player')
        new_product_voice_assistant = request.form.get('voice_assistant')

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

                product.weight = new_product_weight
                product.weight_units = new_product_weight_units

                product.color = new_product_color

                product.subheading = new_product_subheading
                product.description = new_product_description

                product.display_size = new_product_display_size
                product.display_resolution = new_product_display_resolution
                product.operating_system = new_product_operating_system
                product.memory = new_product_memory

                product.brand_id = new_product_brand
                product.category_id = new_product_category

                product.battery_capacity = new_product_battery_capacity

                product.wifi = new_product_wifi == 'y'
                product.bluetooth = new_product_bluetooth == 'y'
                product.nfc = new_product_nfc == 'y'
                product.esim = new_product_esim == 'y'

                product.heart_rate_monitor = new_product_heart_rate_monitor == 'y'
                product.step_counter = new_product_step_counter == 'y'
                product.sleep_tracker = new_product_sleep_tracker == 'y'
                product.gps = new_product_gps == 'y'
                product.water_resistant = new_product_water_resistant == 'y'
                product.music_player = new_product_music_player == 'y'
                product.voice_assistant = new_product_voice_assistant == 'y'

                product.date_edited = datetime.utcnow()
                product.edited = True
                db.session.commit()
                form.product_name.data = ''
                flash('Produkt byl aktualizován.', category='success')
                return redirect(url_for('products.product_page_preview', product_id=product.id, customer=current_user))

    return render_template('edit_smart_watch_product.html', product=product, form=form, customer=current_user)


@products.route('/delete-smart-watch-product/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_smart_watch_product(id):
    product = Product.query.filter_by(id=id).first_or_404()
    watch = SmartWatch.query.filter_by(id=id).first_or_404()

    product_images = ProductImage.query.filter_by(product_id=product.id).all()
    main_image = os.path.join(current_app.config['UPLOAD_FOLDER'], product.product_image)
    os.remove(main_image)
    for image in product_images:
        image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], image.image_name)
        os.remove(image_path)
        db.session.delete(image)
    db.session.delete(product)
    db.session.delete(watch)
    db.session.commit()
    flash('Produkt byl smazán.', category='success')
    return redirect('/products/products-list')
