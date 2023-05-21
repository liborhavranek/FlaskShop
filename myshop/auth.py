""" Libor Havránek App Copyright (C)  23.3 2023 """
import csv

from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_user, current_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from myshop import db
from .forms.login_form import LoginForm
from .forms.registration_form import RegistrationForm
from myshop.models.customer_model import Customer
from .models.brand_model import Brand
from .models.category_model import Category
from .models.mobile_model import Mobile

auth = Blueprint('auth', __name__, template_folder='templates/authenticates')


@auth.route('/')
def authenticate() -> str:
    return render_template('auth.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        customer_data = {
            'username': request.form.get('username'),
            'email': request.form.get('email'),
            'phone_code': request.form.get('phone_code'),
            'phone': request.form.get('phone'),
            'user_password': generate_password_hash(request.form.get('password'), method='sha256'),
            'faktura_first_name': request.form.get('faktura_first_name'),
            'faktura_last_name': request.form.get('faktura_last_name'),
            'faktura_city': request.form.get('faktura_city'),
            'faktura_street': request.form.get('faktura_street'),
            'faktura_zipcode': request.form.get('faktura_zipcode'),
            'dodej_first_name': request.form.get('dodej_first_name'),
            'dodej_last_name': request.form.get('dodej_last_name'),
            'dodej_company': request.form.get('dodej_company'),
            'dodej_city': request.form.get('dodej_city'),
            'dodej_street': request.form.get('dodej_street'),
            'dodej_zipcode': request.form.get('dodej_zipcode'),
            'dodej_info': request.form.get('dodej_info'),
            'dodej_phone_code': request.form.get('dodej_phone_code'),
            'dodej_phone': request.form.get('dodej_phone'),
            'firma_ico': request.form.get('firma_ico'),
            'firma_dic': request.form.get('firma_dic'),
            'firma_bank_acc': request.form.get('firma_bank_acc'),
            'firma_bank_number': request.form.get('firma_bank_number'),
            'firma_spec_symbol': request.form.get('firma_spec_symbol')
        }
        new_customer = Customer(**customer_data)
        db.session.add(new_customer)
        db.session.commit()
        login_user(new_customer, remember=True)
        flash('Profil byl úspěšně vytvořen.', category='success')
        return redirect("/auth/")
    return render_template('register.html', form=form)


@auth.route('/check-email', methods=['POST'])
def check_email():
    email = request.form['email']
    user = Customer.query.filter_by(email=email).first()
    if user:
        return 'taken'
    else:
        return 'available'


@auth.route('/check-username', methods=['POST'])
def check_username():
    username = request.form['username']
    user = Customer.query.filter_by(username=username).first()
    if user:
        return 'taken'
    else:
        return 'available'


@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        user_password = form.password.data
        costumer = Customer.query.filter_by(email=email).first()
        if costumer:
            if check_password_hash(costumer.user_password, user_password):
                print(user_password)
                print(costumer.user_password)
                flash("Úspěšně jsi se přihlásil.", category='success')
                login_user(costumer, remember=True)
                return render_template("index.html", costumer=current_user)
            else:
                flash('Zadal jsi nesprávné heslo.', category='error')
        else:
            flash('Email neexistuje.', category='error')
    return render_template("login.html", form=form, customer=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")


@auth.route('/create-customers')
def create_test_data():
    password = "testtest"
    users = [
        {"username": "admin", "email": "liborhavranek91@gmail.com", "phone": "123456789"},
        {"username": "admin1", "email": "liborseucipython@gmail.com", "phone": "123456789"}
    ]
    brands = [

            {"brand_name": "Apple"},
            {"brand_name": "Samsung"},
            {"brand_name": "Xiaomi"},
            {"brand_name": "Acer"},
            {"brand_name": "Dell"},
            {"brand_name": "HP"},
            {"brand_name": "Asus"},
            {"brand_name": "MSI"},

    ]
    categories = [
        {"category_name": "Mobily"},
        {"category_name": "Hodinky"},
        {"category_name": "Tablety"},
        {"category_name": "Notebooky"},
        {"category_name": "Monitory"},
        {"category_name": "Televize"},
        {"category_name": "Sluchátka"},
        {"category_name": "Herní konzole"},
    ]

    for user in users:
        customer = Customer()
        customer.username = user["username"]
        customer.email = user["email"]
        customer.phone = user["phone"]
        customer.user_password = generate_password_hash(password, method='sha256')
        db.session.add(customer)

    # Log in the first user
    customer = Customer.query.filter_by(username='admin').first()
    login_user(customer)
    db.session.commit()

    for trademark in brands:
        brand = Brand()
        brand.brand_name = trademark["brand_name"]
        db.session.add(brand)
        db.session.commit()

    for cat in categories:
        category = Category()
        category.category_name = cat["category_name"]
        db.session.add(category)
        db.session.commit()

    with open('myshop/products.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            product = Mobile()
            product.product_name = row["product_name"]
            product.price = row["price"]
            product.discount = row["discount"]
            product.stock = row["stock"]

            product.subheading = row["subheading"]
            product.description = row["description"]

            product.visit_count = row["visit_count"]

            product.display_size = row["display_size"]
            product.display_resolution = row["display_resolution"]
            product.operating_system = row["operating_system"]
            product.operating_memory = row["operating_memory"]
            product.memory = row["memory"]

            product.height = row["height"]
            product.height_units = row["height_units"]
            product.width = row["width"]
            product.weight_units = row["weight_units"]
            product.depth = row["depth"]
            product.depth_units = row["depth_units"]
            product.weight = row["weight"]
            product.weight_units = row["weight_units"]

            product.battery_capacity = row["battery_capacity"]
            product.memory_card_slot = bool(row['memory_card_slot'])
            product.face_id = bool(row["face_id"])
            product.touch_screen = bool(row["touch_screen"])
            product.front_camera = row["front_camera"]
            product.back_camera = row["back_camera"]
            product.convertible = bool(row["convertible"])
            product.wifi = bool(row["wifi"])
            product.bluetooth = bool(row["bluetooth"])
            product.nfc = bool(row["nfc"])
            product.processor = row["processor"]
            product.processor_cores = row["processor_cores"]
            product.esim = bool(row["esim"])

            product.color = row["color"]
            product.brand_id = row["brand_id"]
            product.category_id = row["category_id"]
            product.product_image = row["product_image"]
            product.product_type = row["product_type"]

            db.session.add(product)
            db.session.commit()
    return render_template("auth.html", customer=current_user)
