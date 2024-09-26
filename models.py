from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(200))
    phone = db.Column(db.String(20))
    first_name = db.Column(db.String(80), nullable=True, default=" ")  
    last_name = db.Column(db.String(80), nullable=True, default=" ")  
    role = db.Column(db.String(50), nullable=True, default="User")




class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    shoe_detail_id = db.Column(db.Integer, db.ForeignKey('shoe_detail.shoe_detail_id'), nullable=False)
    order_date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    order_status = db.Column(db.String(50), nullable=False)

class Payment(db.Model):
    payment_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'), nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    payment_status = db.Column(db.String(50), nullable=False)
    payment_date = db.Column(db.Date, nullable=False)

class ShoeDetail(db.Model):
    shoe_detail_id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('shoe_category.category_id'), nullable=False)
    shoe_name = db.Column(db.String(100), nullable=False)
    shoe_price = db.Column(db.Float, nullable=False)
    shoe_size = db.Column(db.String(10), nullable=False)
    stock = db.Column(db.Integer, nullable=False)

class ShoeCategory(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(100), nullable=False)

class Gallery(db.Model):
    gallery_id = db.Column(db.Integer, primary_key=True)
    shoe_detail_id = db.Column(db.Integer, db.ForeignKey('shoe_detail.shoe_detail_id'), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
