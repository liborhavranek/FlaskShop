""" Libor Havránek App Copyright (C)  23.3 2023 """

from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_user, current_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from myshop import db
from .forms.login_form import LoginForm
from .forms.registration_form import RegistrationForm
from myshop.models.customer_model import Customer
from .models.brand_model import Brand
from .models.category_model import Category
from .models.product_model import Product

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

    products = [
        {'product_name': 'Iphone 13',
         "price": 799,
         "discount": 5,
         "stock": 20,
         "size": 6.1,
         "size_units": "in",
         "weight": 174,
         "weight_units": "g",
         "color": "stříbrná",
         "subheading": "Nový iPhone 13 - Výkonný a stylový mobilní telefon",
         "description": "Popis produktu: Nový iPhone 13 přináší vysoký výkon a stylový design. Disponuje 6,1palcovým "
                        "Liquid Retina displejem s True Tone technologií a špičkovým fotoaparátem, který vám umožní "
                        "snímat neuvěřitelně detailní fotografie a videa. Procesor A15 Bionic zaručí hladký chod a "
                        "výkonná baterie vám umožní používat telefon až 19 hodin. iPhone 13 je také odolný vůči "
                        "vode a prachu a podporuje nejnovější verzi operačního systému iOS.",
         "brand_id": 1,
         "category_id": 1,
         "product_image": "test_image_iphone_13_1.jpeg"
         },

        {'product_name': 'iPhone 13 Pro',
         'price': 899,
         'discount': 5,
         'stock': 100,
         'size': 6.1,
         'size_units': 'in',
         'weight': 204,
         'weight_units': 'g',
         'color': 'stříbrná',
         'subheading': 'Vylepšený iPhone 13 Pro - Profesionální výkon a funkce',
         'description': 'Popis produktu: iPhone 13 Pro je nejnovější vlajkovou lodí značky Apple. Tento mobilní telefon'
                        ' nabízí profesionální výkon a funkce, díky kterým můžete svůj život zlepšit. Telefon má velký'
                        ' 6,1palcový Super Retina XDR displej s ProMotion technologií, který zobrazuje '
                        'výrazné a detailní barvy. Díky pokročilému systému fotoaparátů s trojitým objektivem můžete'
                        ' snímat skvělé fotografie a videa s vysokým rozlišením, a to i v podmínkách s nízkým'
                        ' osvětlením. Nový procesor A15 Bionic zajišťuje hladký chod a neuvěřitelnou zábavu. '
                        'Telefon obsahuje také vysoce výkonnou baterii, která umožní až 22 hodin hovoru nebo až 75 '
                        'hodin poslechu hudby. Nový iPhone 13 Pro je navíc odolný vůči vodě a prachu, takže vás '
                        'nezklame ani v náročných podmínkách.',
         'brand_id': 1,
         'category_id': 1,
         'product_image': 'test_image_iphone_13_pro_1.jpeg'},

        {'product_name': 'Iphone 13 pro Max',
         "price": 999,
         "discount": 5,
         "stock": 10,
         "size": 6.7,
         "size_units": "in",
         "weight": 238,
         "weight_units": "g",
         "color": "cerna",
         "subheading": "Nový iPhone 13 Pro Max - Výkon a kvalita bez kompromisů",
         "description": "Popis produktu: Nový iPhone 13 Pro Max je špičkou v oblasti mobilních telefonů, který nabízí"
                        " nejvyšší výkon a kvalitu bez kompromisů. Disponuje nejmodernějšími technologiemi a funkcemi, "
                        "které zajistí hladký chod a neuvěřitelnou zábavu. Telefon má velký 6,7palcový"
                        " Super Retina XDR displej s ProMotion technologií, který zobrazuje výrazné a detailní barvy."
                        " Díky pokročilému systému fotoaparátů můžete snímat skvělé fotografie a videa s vysokým"
                        " rozlišením, a to i v podmínkách s nízkým osvětlením. Telefon obsahuje nejnovější procesor"
                        " A15 Bionic a vysoce výkonnou baterii, která umožní až 28 hodin hovoru nebo až 95 hodin"
                        " poslechu hudby. Nový iPhone 13 Pro Max je navíc odolný vůči vodě a prachu, takže vás"
                        " nezklame ani v náročných podmínkách.",
         "brand_id": 1,
         "category_id": 1,
         "product_image": "test_image_iphone_13_pro_max_1.jpeg"
         },
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

    for prod in products:
        product = Product()
        product.product_name = prod["product_name"]
        product.price = prod["price"]
        product.discount = prod["discount"]
        product.stock = prod["stock"]
        product.size = prod["size"]
        product.size_units = prod["size_units"]
        product.weight = prod["weight"]
        product.weight_units = prod["weight_units"]
        product.color = prod["color"]
        product.subheading = prod["subheading"]
        product.description = prod["description"]
        product.brand_id = prod["brand_id"]
        product.category_id = prod["category_id"]
        product.product_image = prod["product_image"]
        db.session.add(product)
        db.session.commit()
    return render_template("auth.html", customer=current_user)
