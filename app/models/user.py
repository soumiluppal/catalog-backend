from flask import url_for
import sqlalchemy as sa
from sqlalchemy.orm import relationship
from app.db import Base

class UserModel(Base):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    full_name = sa.Column(sa.String(60))
    username = sa.Column(sa.String(40), unique=True)
    password = sa.Column(sa.String(40))
    email = sa.Column(sa.String(100), unique=True)

    def __init__(self, full_name, username, password, email):
        self.full_name = full_name
        self.username = username
        self.password = password
        self.email = email
    
    def get_url(self):
        return url_for('api.get_users', id=self.id, _external=True)

    def export_data(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'username': self.username,
            'email': self.email,
            'password': self.password
        }

    def import_data(self, data):
        try:
            self.full_name = data['full_name']
            self.username = data['username']
            self.password = data['password']
            self.email = data['email']
        except KeyError as e:
            print(e)
            #raise ValidationError('Invalid customer: missing ' + e.args[0])
        return self

    def save_to_db(self):
        db_session.add(self)
        db_session.commit()