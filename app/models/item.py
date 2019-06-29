from flask import url_for
import sqlalchemy as sa
from sqlalchemy.orm import relationship
from app import db

class ItemModel(db.Model):
    __tablename__ = 'items'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(40))
    description = sa.Column(sa.String(300))
    price = sa.Column(sa.Integer)
    category_id = sa.Column(sa.Integer, sa.ForeignKey('categories.id'))
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))

    def __init__(self, name, description, price, category_id, user_id):
        self.name = name
        self.description = description
        self.price = price
        self.category_id = category_id
        self.user_id = user_id

    def get_url(self):
        return url_for('api.get_items', id=self.id, _external=True)

    def export_data(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price
        }

    def import_data(self, data):
        try:
            self.name = data['name']
            self.description = data['description']
            self.price = data['price']
        except KeyError as e:
            print(e)
            #raise ValidationError('Invalid customer: missing ' + e.args[0])
        return self

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()