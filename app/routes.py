from flask import Blueprint, jsonify, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app.models import User, db

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/", methods=["GET"])
def default_page():
    """
        메인 페이지
    """
    if request.method == "GET":
        return render_template("main.html")


@user_routes.route("/login", methods=["GET", "POST"])
def login_page():
    """
        로그인 페이지
    """
    if request.method == "GET":
        return render_template("login.html")
    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({"message": "Invalid email or password"}), 401

    login_user(user)
    return render_template("homePage.html"), 200

@user_routes.route("/logout", methods=["GET"])
@login_required
def logout():
    """
        로그아웃 페이지
    """
    logout_user()
    return jsonify({"message": "Logged out successfully!"}), 200

@user_routes.route("/register", methods=["GET", "POST"])
def register():
    """
        회원등록 페이지
    """
    if request.method == "GET":
        flash("Registration successful! Please log in.")
        return redirect(url_for("user_routes.login_page"))

    # POST 요청 처리
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    if User.query.filter_by(email=email).first():
        return jsonify({"message": "Email already registered"}), 400

    new_user = User(name=name, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return render_template("success.html")

@user_routes.route("/protected", methods=["GET"])
@login_required
def protected():
    return jsonify({"message": f"Hello, {current_user.name}! This is a protected route."}), 200


@user_routes.route("/homePage", methods=["GET"])
@login_required
def homePage():
    """
        이커머스 쇼핑몰 홈페이지
    """
    return render_template("homePage.html")