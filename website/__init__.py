from os import path
from flask import Flask
from flask_login import LoginManager, login_manager
from flask_sqlalchemy import SQLAlchemy
from flask.helpers import send_from_directory

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Pvn4QhMGIeN9XXk0351O"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    from .views import views, internal_server_error, page_not_found, page_forbidden
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)
    app.register_error_handler(403, page_forbidden)

    from .models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    @app.route('/assets/<path:path>')
    def send_assets(path):
        return send_from_directory('assets', path)

    return app

def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("Created database!")