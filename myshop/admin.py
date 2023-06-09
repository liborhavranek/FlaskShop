""" Libor Havránek App Copyright (C)  23.3 2023 """

from flask import Blueprint, render_template
from flask_login import current_user

admin = Blueprint("admin", __name__, template_folder="templates")


@admin.route("/")
def admin_page() -> str:
    return render_template("admin.html", customer=current_user)
