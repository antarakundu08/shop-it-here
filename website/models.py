from . import db
from flask_login import UserMixin

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000), nullable= False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(200))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    fullname = db.Column(db.String(150))