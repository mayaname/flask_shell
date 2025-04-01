"""
Program: __init__
Author: Maya Name
Creation Date: 03/05/2025
Revision Date: 
Description: Init for Flask application


Revisions:

"""

from flask import Flask
from .extensions import db, login_manager
from .auth import auth
from .models import User
from .routes import pages


def create_app():
    app = Flask(__name__)

    # Sets config for development
    app.config['SECRET_KEY'] = 'mysecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Set view to login route 
    login_manager.login_view = 'pages.login'
    login_manager.login_message = 'You are not authorized to modify site content.'
    login_manager.login_message_category = 'warning'

    # Get user by id for login manager
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    app.register_blueprint(pages)
    app.register_blueprint(auth)

    return app