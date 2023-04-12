""" Libor Havránek App Copyright (C)  1.4 2023 """

from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError, Regexp, Optional

from myshop.models import Customer


class RegistrationForm(FlaskForm):
    csrf_token = HiddenField()
    username = StringField('Přihlašovací jméno:', validators=[DataRequired(), Length(min=5, max=30)])
    email = StringField('Email:', validators=[DataRequired(), Length(min=10, max=50),  Email()])
    phone_code = SelectField('Kód:', choices=[('+420', '+420'), ('+421', '+421')])
    phone = StringField('Telefon:', validators=[DataRequired(), Length(min=9, max=9), Regexp('^[0-9]*$')])
    password = PasswordField('Heslo:', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Potvrdit heslo:', validators=[DataRequired(), EqualTo('password')])

    faktura_first_name = StringField('Jméno:')
    faktura_last_name = StringField('Příjmení:')
    faktura_city = StringField('Město:')
    faktura_street = StringField('Ulice:')
    faktura_zipcode = StringField('PSČ:', validators=[Optional(), Length(min=5, max=5)])

    dodej_first_name = StringField('Jméno:')
    dodej_last_name = StringField('Příjmení:')
    dodej_company = StringField('Firma:')
    dodej_city = StringField('Město:')
    dodej_street = StringField('Ulice:')
    dodej_zipcode = StringField('PSČ:', validators=[Optional(), Length(min=5, max=5)])
    dodej_info = StringField('Info(např. patro):')
    dodej_phone_code = SelectField('Kód:', choices=[('+420', '+420'), ('+421', '+421')])
    dodej_phone = StringField('Telefon:', validators=[Optional(), Length(min=9, max=9), Regexp('^[0-9]*$')])

    firma_ico = StringField('IČO:', validators=[Optional(), Length(min=8, max=8)])
    firma_dic = StringField('DIČ:', validators=[Optional(), Length(min=8, max=15)])
    firma_bank_acc = StringField('Číslo účtu:')
    firma_bank_number = StringField('Kód banky:')
    firma_spec_symbol = StringField('Specifický symbol:')

    submit = SubmitField('Registrovat')

    def validate_confirm_password(self, confirm_password):
        if len(self.password.data) < 8:
            flash('Heslo musí mít alespoň 8 znaků.', 'error')
            raise ValidationError('Heslo musí mít alespoň 8 znaků.')
        if self.password.data != confirm_password.data:
            flash('Heslo a potvrzení hesla se musí shodovat.', 'error')
            return False
        return True

    def validate_email(self, email):
        customer = Customer.query.filter_by(email=email.data).first()
        if customer:
            flash('Tento email je už zaregistrován v naší databázi.', 'error')
            raise ValidationError('Email is already in use.')

    def validate_username(self, username):
        customer = Customer.query.filter_by(username=username.data).first()
        if customer:
            flash("Toto uživatelské jméno už je zaregistrované v naší databázi.", "error")
            raise ValidationError('Username is already in use.')

    def validate_faktura_zipcode(self, faktura_zipcode):
        if faktura_zipcode.data and len(faktura_zipcode.data) != 5:
            flash('PSČ musí mít přesně 5 číslic.', 'error')
            raise ValidationError('PSČ musí mít přesně 5 číslic.')

    def validate_dodej_zipcode(self, dodej_zipcode):
        if dodej_zipcode.data and len(dodej_zipcode.data) != 5:
            flash('PSČ musí mít přesně 5 číslic.', 'error')
            raise ValidationError('PSČ musí mít přesně 5 číslic.')
