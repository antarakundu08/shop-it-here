import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from website.models import Product
from website import db, create_app


app=create_app()


with app.app_context():
    db.create_all()

    product1 = Product(name= 'Product 1', description= 'Product 1 description', price = 170.99, image_url = 'website/static/camera.jpg')
    product2 = Product(name= 'Product 2', description= 'Product 2 description', price = 170.99, image_url = 'website/static/camera.jpg')
    product3 = Product(name= 'Product 3', description= 'Product 3 description', price = 170.99, image_url = 'website/static/camera.jpg')
    product4 = Product(name= 'Product 4', description= 'Product 4 description', price = 170.99, image_url = 'website/static/camera.jpg')
    product5 = Product(name= 'Product 5', description= 'Product 5 description', price = 170.99, image_url = 'website/static/camera.jpg')
    product6 = Product(name= 'Product 6', description= 'Product 6 description', price = 170.99, image_url = 'website/static/camera.jpg')
    product7 = Product(name= 'Product 7', description= 'Product 7 description', price = 170.99, image_url = 'website/static/camera.jpg')
    product8 = Product(name= 'Product 8', description= 'Product 8 description', price = 170.99, image_url = 'website/static/camera.jpg')
    product9 = Product(name= 'Product 9', description= 'Product 9 description', price = 170.99, image_url = 'website/static/camera.jpg')
    product10 = Product(name= 'Product 10', description= 'Product 10 description', price = 170.99, image_url = 'website/static/camera.jpg')
    product11 = Product(name= 'Product 11', description= 'Product 11 description', price = 170.99, image_url = 'website/static/camera.jpg')
    product12 = Product(name= 'Product 12', description= 'Product 12 description', price = 170.99, image_url = 'website/static/camera.jpg')
    product13 = Product(name= 'Product 13', description= 'Product 13 description', price = 170.99, image_url = 'website/static/camera.jpg')
    product14 = Product(name= 'Product 14', description= 'Product 14 description', price = 170.99, image_url = 'website/static/camera.jpg')
    product15 = Product(name= 'Product 15', description= 'Product 15 description', price = 170.99, image_url = 'website/static/camera.jpg')
    product16 = Product(name= 'Product 16', description= 'Product 16 description', price = 170.99, image_url = 'website/static/camera.jpg')

    items = [product1, product2, product3, product4, product5, product6, product7, product8, product9, product10, product11, product12, product13, product14, product15, product16]
    db.session.add_all(items)
    db.session.commit()