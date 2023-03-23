""" Libor Havránek App Copyright (C)  23.3 2023 """

from flask import Blueprint, render_template

admin = Blueprint('admin', __name__, template_folder='templates')


@admin.route('/')
def admin_page() -> str:
    return render_template('admin.html')
