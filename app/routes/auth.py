from flask import(
  session,
  render_template,
  redirect,
  url_for,
  flash,
  request,
  Blueprint
)
from werkzeug.security import generate_password_hash, check_password_hash

from app.models import User, Chat
from app import db

auth_bp = Blueprint("auth" , __name__)


#Home Login 
@auth_bp.route("/")
def home():
    if "id" not in session:
        return redirect(url_for("auth.login"))

    return redirect(url_for("dashboard.dashboard"))

#Register  Login 

@auth_bp.route("/register" ,methods = ["GET" , "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")

        user_exit = User.query.filter_by(email=email).first()
        if user_exit:
            flash(f"User Already Exit")
            return redirect(url_for("auth.login"))

        hash_passwoed = generate_password_hash(password)

        new_user = User(
            email = email,
            name = name,
            password = hash_passwoed
        )
        db.session.add(new_user)
        db.session.commit()

        flash(f"Register Successfull! ✔")
        return redirect(url_for("auth.login"))

    return render_template("register.html")



@auth_bp.route("/login" , methods = ["GET" , "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session["id"] = user.id
            session["email"] = user.email

            flash(f"Login successfull! ✔")
            return redirect(url_for("dashboard.dashboard"))

        flash(f"Wrong username or password! ")

    return render_template("login.html")



#logout logic


@auth_bp.route("/logout")
def logout():

    session.pop("id", None)

    return redirect(url_for("auth.login"))
    flash(f"Logout User 👨🏼‍🎓")
   





