""" Libor Havránek App Copyright (C)  1.4 2023 """

from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegistrationForm(FlaskForm):
    csrf_token = HiddenField()
    username = StringField('Přihlašovací jméno:', validators=[DataRequired(), Length(min=4, max=30)])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    phone_code = StringField('Kód:')
    phone = StringField('Telefon:')
    password = PasswordField('Heslo:', validators=[DataRequired()])
    confirm_password = PasswordField('Potvrdit heslo:', validators=[DataRequired(), EqualTo('password')])

    faktura_first_name = StringField('Jméno:')
    faktura_last_name = StringField('Příjmení:')
    faktura_city = StringField('Město:')
    faktura_street = StringField('Ulice:')
    faktura_zipcode = StringField('PSČ:')

    dodej_first_name = StringField('Jméno:')
    dodej_last_name = StringField('Příjmení:')
    dodej_company = StringField('Firma:')
    dodej_city = StringField('Město:')
    dodej_street = StringField('Ulice:')
    dodej_zipcode = StringField('PSČ:')
    dodej_info = StringField('Info(např. patro):')
    dodej_phone_code = StringField('Kód:')
    dodej_phone = StringField('Telefon:')

    firma_ico = StringField('IČO:')
    firma_dic = StringField('DIČ:')
    firma_bank_acc = StringField('Číslo účtu:')
    firma_bank_number = StringField('Kód banky:')
    firma_spec_symbol = StringField('Specifický symbol:')

    submit = SubmitField('Registrovat')


    def validate_confirm_password(self, confirm_password):
        if self.password.data != confirm_password.data:
            flash('Heslo a potvrzení hesla se musí shodovat.', 'error')
            return False
        return True
