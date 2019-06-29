from marshmallow import Schema, fields, ValidationError, validates
from app.models.user import UserModel

class UserSchema(Schema):
    id = fields.Integer()
    full_name = fields.Str(required=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)

    @validates('username')
    def validate_username(self, username):
        if len(username) > 40:
            raise ValidationError('Username must be less than 40 characters long')
        elif len(username) < 5:
            raise ValidationError('Username must be at least 5 characters long.')
        elif UserModel.query.filter_by(username=username).first():
            raise ValidationError('The username has been taken.')

    @validates('full_name')
    def validate_name(self, full_name):
        if len(full_name) > 60:
            raise ValidationError('Full name must be less than 60 characters long.')

    @validates('email')
    def validate_email(self, email):
        if UserModel.query.filter_by(email=email).first():
            raise ValidationError('The email has already been taken.')

    @validates('password')
    def validate_password(self, password):
        if len(password) < 8:
            raise ValidationError('Password must be less than 8 characters long.')