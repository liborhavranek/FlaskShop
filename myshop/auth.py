""" Libor Havránek App Copyright (C)  23.3 2023 """

from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_user, current_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from myshop import db
from .forms.forms import RegistrationForm
from .models import Customer

auth = Blueprint('auth', __name__, template_folder='templates/authenticates')


@auth.route('/')
def authenticate() -> str:
    return render_template('auth.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():

    form = RegistrationForm()
    if form.validate_on_submit():
        # ______________user_____________________
        username = request.form.get("username")
        email = request.form.get("email")
        phone_code = request.form.get("phone_code")
        phone = request.form.get("phone")
        password = request.form.get("password")
        # --------------- Fakturacni udaje ---------------------
        faktura_first_name = request.form.get("faktura_first_name")
        faktura_last_name = request.form.get("faktura_last_name")
        faktura_city = request.form.get("faktura_city")
        faktura_street = request.form.get("faktura_street")
        faktura_zipcode = request.form.get("faktura_zipcode")

        # ---------------Dodaci udaje ---------------------------------

        dodej_first_name = request.form.get("dodej_first_name")
        dodej_last_name = request.form.get("dodej_last_name")
        dodej_company = request.form.get("dodej_company")
        dodej_city = request.form.get("dodej_city")
        dodej_street = request.form.get("dodej_street")
        dodej_zipcode = request.form.get("dodej_zipcode")
        dodej_info = request.form.get("dodej_info")
        dodej_phone_code = request.form.get("dodej_phone_code")
        dodej_phone = request.form.get("dodej_phone")

        # -------------------Firemní údaje -------------------------------------

        firma_ico = request.form.get("firma_ico")
        firma_dic = request.form.get("firma_dic")
        firma_bank_acc = request.form.get("firma_bank_acc")
        firma_bank_number = request.form.get("firma_bank_number")
        firma_spec_symbol = request.form.get("firma_spec_symbol")

        new_costumer = Customer()
        new_costumer.username = username
        new_costumer.email = email
        new_costumer.phone_code = phone_code
        new_costumer.phone = phone
        new_costumer.user_password = generate_password_hash(password, method='sha256')

        new_costumer.faktura_first_name = faktura_first_name
        new_costumer.faktura_last_name = faktura_last_name
        new_costumer.faktura_city = faktura_city
        new_costumer.faktura_street = faktura_street
        new_costumer.faktura_zipcode = faktura_zipcode

        new_costumer.dodej_first_name = dodej_first_name
        new_costumer.dodej_last_name = dodej_last_name
        new_costumer.dodej_info = dodej_company
        new_costumer.dodej_city = dodej_city
        new_costumer.dodej_street = dodej_street
        new_costumer.dodej_zipcode = dodej_zipcode
        new_costumer.dodej_info = dodej_info
        new_costumer.dodej_phone_code = dodej_phone_code
        new_costumer.dodej_phone = dodej_phone

        new_costumer.firma_ico = firma_ico
        new_costumer.firma_dic = firma_dic
        new_costumer.firma_bank_acc = firma_bank_acc
        new_costumer.firma_bank_number = firma_bank_number
        new_costumer.firma_spec_symbol = firma_spec_symbol

        db.session.add(new_costumer)
        db.session.commit()
        login_user(new_costumer, remember=True)
        flash('Profil byl úspěšně vytvořen.', category='success')
        return render_template('login.html', costumer=current_user)

    return render_template('register.html', customer=current_user, form=form)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        user_password = request.form.get("password")
        costumer = Customer.query.filter_by(email=email).first()
        if costumer:
            if check_password_hash(costumer.user_password, user_password):
                flash("Úspěšně jsi se přihlásil.", category='success')
                login_user(costumer, remember=True)
                return render_template("index.html", costumer=current_user)
            else:
                flash('Zadal jsi nesprávné heslo.', category='error')
        else:
            flash('Email neexistuje.', category='error')

    return render_template("login.html", customer=current_user)


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
