from flask import url_for
import sqlalchemy as sa
from sqlalchemy.orm import relationship
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class UserModel(db.Model):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    full_name = sa.Column(sa.String(60))
    username = sa.Column(sa.String(40), unique=True)
    password = sa.Column(sa.String(200))
    email = sa.Column(sa.String(100), unique=True)
    items = relationship('ItemModel', backref='item', lazy='dynamic', cascade='all, delete-orphan')

    def __init__(self, full_name, username, password, email):
        self.full_name = full_name
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email

    def export_data(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'username': self.username,
            'email': self.email,
            'password': self.password
        }

    def import_data(self, data):
        self.full_name = data['full_name']
        self.username = data['username']
        self.password = self.password = generate_password_hash(data['password'])
        self.email = data['email']
        return self

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()