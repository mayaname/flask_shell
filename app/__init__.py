"""
Program: __init__
Author: Maya Name
Creation Date: 03/05/2025
Revision Date: 
Description: Init for Flask  application


Revisions:

"""

from flask import Flask
# from .extensions import db, migrate
from .auth import auth
# from .models import User
from .routes import pages


def create_app():
    app = Flask(__name__)

    # Sets config for development
    app.config['SECRET_KEY'] = 'mysecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

    # Initialize extensions
    # db.init_app(app)
    # migrate.init_app(app, db)

    # Set view to login route 

    # Get user by id for login manager

    # Register blueprints
    app.register_blueprint(pages)
    app.register_blueprint(auth)

    return app