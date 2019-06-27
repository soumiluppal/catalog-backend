from marshmallow import Schema, fields

class CategorySchema(Schema):
    id = fields.Integer()
    name = fields.Str(
        required=True
    )
    description = fields.Str(
        required=True
    )