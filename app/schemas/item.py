from marshmallow import Schema, fields, ValidationError, validates
from app.models.item import ItemModel
from app.models.category import CategoryModel

class ItemSchema(Schema):
    id = fields.Integer()
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Integer(required=True)
    category_id = fields.Integer(required=True)
    user_id = fields.Integer(required=True)

    @validates('name')
    def validate_name(self, name):
        if len(name) > 40:
            raise ValidationError('Item name must be less than 40 characters long.')
        elif len(name) < 3:
            raise ValidationError('Item name must be atleast 3 characters long.')

    @validates('description')
    def validate_desc(self, description):
        if len(description) > 300:
            raise ValidationError('Item description must be less than 300 characters long.')
        elif len(description) < 5:
            raise ValidationError('Item description must be atleast 5 characters long.')

    @validates('price')
    def validate_price(self, price):
        if price < 0:
            raise ValidationError('Price must be atleast $0.')

    @validates('category_id')
    def validate_category(self, category_id):
        if not CategoryModel.query.filter_by(id=category_id).first():
            raise ValidationError('No such category exists.')