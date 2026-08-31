from flask import(
  session,
  render_template,
  redirect,
  url_for,
  flash,
  request,
  Blueprint
)

from app.models import User, Chat
from app import db

auth_bp = Blueprint("auth" , __name__)


#Home Login 
@auth_bp.route("/")
def home():
    if "user" not in session:
        return redirect(url_for("auth.login"))

    return redirect(url_for("dashboard.dashboard"))

#Register 



