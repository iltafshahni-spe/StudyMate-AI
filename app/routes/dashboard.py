
from flask import Blueprint, render_template , session ,redirect , url_for
from app import db

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard")
def dashboard():
    if "id" not in session:
        return redirect(url_for("auth.login"))

    return render_template("dashboard.html")