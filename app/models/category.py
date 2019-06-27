from flask import url_for
import sqlalchemy as sa
from sqlalchemy.orm import relationship
from app.db import Base, db_session

class CategoryModel(Base):
    __tablename__ = 'categories'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(40), unique=True)
    description = sa.Column(sa.String(300))
    items = relationship('ItemModel')

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_url(self):
        return url_for('api.get_categories', id=self.id, _external=True)

    def export_data(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }

    def import_data(self, data):
        try:
            self.name = data['name']
            self.description = data['description']
        except KeyError as e:
            print(e)
            #raise ValidationError('Invalid customer: missing ' + e.args[0])
        return self

    def save_to_db(self):
        db_session.add(self)
        db_session.commit()
