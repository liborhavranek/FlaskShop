""" Libor Havránek App Copyright (C)  23.3 2023 """

from flask import Blueprint, render_template, request, flash
from flask_login import login_user, current_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from myshop import db
from .models import Customer

auth = Blueprint('auth', __name__, template_folder='templates/authenticates')


@auth.route('/')
def authenticate() -> str:
    return render_template('auth.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # ______________user_____________________
        username = request.form.get("username")
        email = request.form.get("email")
        phone_code = request.form.get("phone_code")
        phone = request.form.get("phone")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        if password1 != password2:
            flash('Heslo a potvrzení hesla se musí shodovat.', category='error')
        else:
            new_costumer = Customer()
            new_costumer.username = username
            new_costumer.email = email
            new_costumer.phone_code = phone_code
            new_costumer.phone = phone
            new_costumer.password = generate_password_hash(password1, method='sha256')
            db.session.add(new_costumer)
            db.session.commit()
            login_user(new_costumer, remember=True)
            flash('Profil byl úspěšně vytvořen.', category='success')
            return render_template('login.html', costumer=current_user)

    return render_template('register.html', customer=current_user)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        costumer = Customer.query.filter_by(email=email).first()
        if costumer:
            if check_password_hash(costumer.password, password):
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
    return render_template("index.html", customer=current_user)


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
