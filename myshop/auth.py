""" Libor Havránek App Copyright (C)  23.3 2023 """

from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_user, current_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from myshop import db
from .forms.login_form import LoginForm
from .forms.registration_form import RegistrationForm
from .models import Customer

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
    password = "test"
    users = [
        {"username": "testuser1", "email": "testuser1@example.com"},
        {"username": "testuser2", "email": "testuser2@example.com"}
    ]
    for user in users:
        customer = Customer()
        customer.username = user["username"]
        customer.email = user["email"]
        customer.password = generate_password_hash(password, method='sha256')
        db.session.add(customer)
    db.session.commit()
    return render_template("auth.html", customer=current_user)
