from flask import request, jsonify
from . import api
from app.models.category import CategoryModel
from app.models.user import UserModel
from app.schemas.user import UserSchema

@api.route('/user', methods=['POST'])
def new_user():
    user_data = request.json
    schema = UserSchema()
    schema.load(user_data)
    user = UserModel(user_data['full_name'], user_data['username'], user_data['password'], user_data['email'])
    user.save_to_db()
    return jsonify({'id': user.id,
                    'username': user.username,
                    'full_name': user.full_name,
                    'password': user.password,
                    'email': user.email}), 201