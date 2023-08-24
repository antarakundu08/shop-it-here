from flask import Blueprint, render_template, session, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from . import models, db
from .models import Product, User, CartItem
from collections import defaultdict

views = Blueprint('views', __name__)

@views.route('/')
def home():
    products = Product.query.all()
    return render_template("home.html",products=products, user=current_user)

@views.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get(product_id)
    return render_template("product_detail.html",product=product, user=current_user)

@views.route('/shopping_cart/<int:product_id>')
def shopping_cart(product_id):
    if not current_user.is_authenticated:
        return redirect(url_for("auth.login"))

    user_id = session['_user_id']
    user = User.query.get(user_id)
    product = Product.query.get(product_id)

    if user and product:
        cart_item = CartItem.query.filter_by(user_id=user_id, product_id=product_id).first()
        
        if cart_item:
            cart_item.quantity+=1
        else:
            cart_item=CartItem(user_id=user_id, product_id=product_id, quantity=1)
            db.session.add(cart_item)
    
        db.session.commit()
        flash(f'{product.name} has been added to cart successfully!', 'success')
    else:
        flash(f'Error adding product to cart', 'danger')
    return redirect(request.referrer)

@views.route('/mycart', methods=['GET', 'POST'])
def mycart():
    if not current_user.is_authenticated:
        flash('Please login to view your cart', 'warning')
        return redirect(url_for("auth.login"))
    
    user_id = session['_user_id']
    user = User.query.get(user_id)
    cart_item = CartItem.query.filter_by(user_id=user_id).all()
    total=0
    product_dict=defaultdict(Product)
    for item in cart_item:
        product = Product.query.get(item.product_id)
        product_dict[item]=product
        total += product.price*item.quantity

    if request.method == 'POST':
        card_number = request.form['card_number']
        card_expiry = request.form['card_expiry']
        card_cvv = request.form['card_cvv']
        print('--------------------')

        if card_number == '1234567890123456' and card_expiry == '12/30' and card_cvv == '123':
            flash('Card information is invalid. Please try again', 'error')
        else:
            for item in cart_item:
                db.session.delete(item)

            db.session.commit()
            flash('Payment Successful. Thank you for your order!', 'success')
            return redirect(url_for('views.home'))

    return render_template('mycart.html', product_dict=product_dict, total=total, user=current_user)


@views.route('/remove_from_cart/<int:item_id>')
def remove_from_cart(item_id):
    if current_user.is_authenticated():
        cart_item = CartItem.query.get(item_id=item_id)
        if cart_item:
            db.session.delete(cart_item)
            db.session.commit()
            flash('Item removed from cart.', 'success')
        else:
            flash('Item not found.', 'danger')
    return redirect(url_for('views.mycart'))


@views.route('/remove_one_from_cart/<int:item_id>')
def remove_one_from_cart(item_id):
    if current_user.is_authenticated:
        user_id = session['_user_id']
        cart_item = CartItem.query.filter_by(id=item_id, user_id=user_id).first()

        if cart_item:
            if cart_item.quantity > 1:
                cart_item.quantity -=1
                db.session.commit()
            else:
                db.session.delete(cart_item)
                db.session.commit()
                flash('Item removed from cart.', 'success')
        else:
            flash('Item not found in cart.', 'danger')
    
    return redirect(url_for('views.mycart'))

@views.route('/checkout')
def checkout():
    user_id = session['_user_id']
    user = User.query.get(user_id)
    cart_item = CartItem.query.filter_by(user_id=user_id).all()
    total=0
    product_dict=defaultdict(Product)
    for item in cart_item:
        product = Product.query.get(item.product_id)
        product_dict[item]=product
        total += product.price*item.quantity
    
    
    return render_template('checkout.html', total=total, user=current_user)
