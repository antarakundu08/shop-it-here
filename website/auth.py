from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Product
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Login successful", category="success")
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect password, Please Try Again!", category="error")
        else:
            flash("Email does not exist", category="error")
    data = request.form
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        fullname = request.form.get('fullname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists", category="error")
        elif len(email) <6:
            flash("Enter a valid email address", category="error")
        elif len(fullname) <3:
            flash("Enter a valid name", category="error")
        elif password1 != password2:
            flash("Passwords do not match", category="error")
        elif len(password1)<7:
            flash("Password must be at least 7 characters", category="error")
        else:
            # add user to database
            new_user  = User(email = email, fullname = fullname, password = generate_password_hash(password1, method="sha256"))
            db.session.add(new_user)
            db.session.commit()

            flash("Account created", category="success")
            return redirect(url_for('views.home'))
    return render_template("register.html",user=current_user)



