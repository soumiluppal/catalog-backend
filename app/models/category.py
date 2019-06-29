from flask import url_for
import sqlalchemy as sa
from sqlalchemy.orm import relationship
from app import db

class CategoryModel(db.Model):
    __tablename__ = 'categories'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(40), unique=True)
    description = sa.Column(sa.String(300))
    items = relationship('ItemModel', backref='category', lazy='dynamic', cascade='all, delete-orphan')

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def export_data(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }

    def import_data(self, data):
        self.name = data['name']
        self.description = data['description']
        return self

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
