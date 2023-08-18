from flask import Blueprint, render_template
from flask_login import login_user, login_required, logout_user, current_user
from . import models
from .models import Product

views = Blueprint('views', __name__)

@views.route('/')

def home():
    products = Product.query.all()
    return render_template("home.html",products=products, user=current_user)


@views.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get(product_id)
    return render_template("product_detail.html",product=product, user=current_user)

@views.route('/mycart/<int:product_id>')
def shopping_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        if 'cart' not in session:
            session['cart'] = []
        session['cart'].append(product)
        return redirect((url_for('home')))
    else:
        return 'Product not found'

# @views.route('/cart')
# def add_to_cart(product_id, quantity):
#     product = Product.query.get(product_id)
#     if product:
#         # Get or create the user's cart
#         cart = session.get('cart',{})

#         # Add the product to the cart
#         if product_id in cart:
#             cart[product_id] +=quantity
#         else:
#             cart[product_id] = quantity
        
#         session['cart'] = cart
#         flash(f'{product.name} added to cart.', 'success')
    
#     else:
#         flash('Product not found.', 'danger')
