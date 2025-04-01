"""
Program: Models
Author: Maya Name
Creation Date: 03/05/2025
Revision Date: 
Description: Models for Flask application


Revisions:

"""




from flask_login import UserMixin
import sqlalchemy as sa
import sqlalchemy.orm as so
from typing import Optional
from .extensions import db 
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    password: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User: {self.username}>'