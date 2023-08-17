from flask import Blueprint, render_template
from flask_login import login_user, login_required, logout_user, current_user
from . import models
from .models import Product

views = Blueprint('views', __name__)

@views.route('/')

def home():
    products = Product.query.all()
    return render_template("home.html",products=products, user=current_user)
