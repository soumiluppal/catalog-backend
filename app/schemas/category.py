from marshmallow import Schema, fields, ValidationError, validates, post_load
from app.models.category import CategoryModel

class CategorySchema(Schema):
    id = fields.Integer()
    name = fields.Str(required=True)
    description = fields.Str(required=True)

    @validates('name')
    def validate_name(self, name):
        if len(name) > 40:
            raise ValidationError('Category name must be less than 40 characters long.')
        elif len(name) < 3:
            raise ValidationError('Category name must be atleast 3 characters long.')
        elif CategoryModel.query.filter_by(name=name).first():
            print("OH GOD CHECK")
            raise ValidationError('Category already exists.')

    @validates('description')
    def validate_desc(self, description):
        if len(description) > 300:
            raise ValidationError('Category description must be less than 300 characters long.')
        elif len(description) < 5:
            raise ValidationError('Category description must be atleast 5 characters long.')

