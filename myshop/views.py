""" Libor Havránek App Copyright (C)  23.3 2023 """

from flask import Blueprint, render_template

views = Blueprint('views', __name__, template_folder='templates')


@views.route('/')
def view() -> str:
    return render_template('views.html')
