from flask import (
Blueprint,
session,
render_template,
redirect,
url_for,
flash,
request
)

import pyotp
import qrcode
import os

from app import db
from app.models import User

two_factor_bp = Blueprint("two_factor", __name__)

@two_factor_bp.route("/setup-2fa")
def setup_2fa():


    if "id" not in session:
        return redirect(url_for("auth.login"))

    user = User.query.get(session["id"])

    if not user:
        return redirect(url_for("auth.login"))

    if not user.totp_secret:
        user.totp_secret = pyotp.random_base32()
        db.session.commit()

    totp = pyotp.TOTP(user.totp_secret)

    uri = totp.provisioning_uri(
        name=user.email,
        issuer_name="StudyMate AI"
    )

    qr = qrcode.make(uri)

    qr_path = os.path.join(
        "app",
        "static",
        "totp_qr.png"
    )

    qr.save(qr_path)

    return render_template("setup-2fa.html")
    

@two_factor_bp.route("/verify-2fa", methods=["GET", "POST"])
def verify_2fa():

    
    if "id" not in session:
        return redirect(url_for("auth.login"))

    user = User.query.get(session["id"])

    if not user or not user.totp_secret:
        return redirect(url_for("two_factor.setup_2fa"))

    if request.method == "POST":

        code = request.form.get("code", "").strip()

        totp = pyotp.TOTP(user.totp_secret)

        if totp.verify(code):

            user.two_factor_enabled = True
            db.session.commit()

            session["2fa_verified"] = True

            flash(
                "Two-factor authentication enabled.",
                "success"
            )

            return redirect(
                url_for("dashboard.dashboard")
            )

        flash(
            "Invalid authentication code.",
            "error"
        )

    return render_template("verify-2fa.html")
