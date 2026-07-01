from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from flask_login import current_user

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from extensions import db
from models.user import User

auth_bp = Blueprint(
    "auth",
    __name__
)

#signup route

@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        role = request.form["role"]

        existing = User.query.filter_by(
            email=email
        ).first()

        if existing:
            flash("Email already exists")
            return redirect(url_for("auth.signup"))

        hashed_password = generate_password_hash(
            password
        )

        user = User(
            name=name,
            email=email,
            password=hashed_password,
            role=role,
            approved=(role == "student")
        )

        db.session.add(user)
        db.session.commit()

        flash("Account Created")

        return redirect(
            url_for("auth.login")
        )

    return render_template("signup.html")

#login route

@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:

        if current_user.role == "student":
            return redirect(url_for("student.dashboard"))

        elif current_user.role == "organizer":
            return redirect(url_for("organizer.dashboard"))

        elif current_user.role == "admin":
            return redirect(url_for("admin.dashboard"))

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(
            email=email
        ).first()

        if not user:
            flash("User not found")
            return redirect(url_for("auth.login"))

        if not check_password_hash(
            user.password,
            password
        ):
            flash("Invalid Password")
            return redirect(url_for("auth.login"))

        if (
            user.role == "organizer"
            and not user.approved
        ):
            flash("Waiting for admin approval")
            return redirect(url_for("auth.login"))

        login_user(user)

        if user.role == "student":
            return redirect(url_for("student.dashboard"))

        elif user.role == "organizer":
            return redirect(url_for("organizer.dashboard"))

        elif user.role == "admin":
            return redirect(url_for("admin.dashboard"))

    return render_template("login.html")

#logout

@auth_bp.route("/logout")
@login_required
def logout():

    logout_user()

    flash("Logged Out")

    return redirect(
        url_for("auth.login")
    )
