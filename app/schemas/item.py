from marshmallow import Schema, fields

class ItemSchema(Schema):
    id = fields.Integer()
    name = fields.Str(
        required=True
    )
    description = fields.Str(
        required=True
    )
    category_id = fields.Integer(
        required=True
    )
    user_id = fields.Integer(
        required=True
    )