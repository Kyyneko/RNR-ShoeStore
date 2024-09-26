from flask import Flask
from config import Config
from models import db
from flask_migrate import Migrate  # Import Flask-Migrate
from routes.users import users_bp
from routes.orders import orders_bp
from routes.payments import payments_bp
from routes.shoes import shoes_bp
from routes.categories import categories_bp
from routes.gallery import gallery_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Inisialisasi Flask-Migrate
migrate = Migrate(app, db)

app.register_blueprint(users_bp)
app.register_blueprint(orders_bp)
app.register_blueprint(payments_bp)
app.register_blueprint(shoes_bp)
app.register_blueprint(categories_bp)
app.register_blueprint(gallery_bp)

if __name__ == '__main__':
    app.run(debug=True)
