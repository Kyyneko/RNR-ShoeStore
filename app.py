from flask import Flask
from config import Config
from models import db
from flask_migrate import Migrate
from routes.users import users_bp
from routes.orders import orders_bp
from routes.payments import payments_bp
from routes.shoes import shoes_bp
from routes.categories import categories_bp
from routes.gallery import gallery_bp
from routes.wallet import wallet_bp
from routes.cart import cart_bp
from routes.wishlist import wishlist_bp
from routes.discount import discount_bp
from routes.search_history import search_history_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(users_bp)
app.register_blueprint(orders_bp)
app.register_blueprint(payments_bp)
app.register_blueprint(shoes_bp)
app.register_blueprint(categories_bp)
app.register_blueprint(gallery_bp)
app.register_blueprint(wallet_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(wishlist_bp)
app.register_blueprint(discount_bp)
app.register_blueprint(search_history_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)