from flask import request, jsonify
from . import api
from app.models.category import CategoryModel
from app.schemas.category import CategorySchema
from flask_jwt import jwt_required
from marshmallow import ValidationError

@api.route('/categories', methods=['GET'])
def get_categories():
    return jsonify({'categories': [category.export_data() for category in
                                    CategoryModel.query.all()]})

@api.route('/categories', methods=['POST'])
def new_category():
    cat_data = request.json
    schema = CategorySchema()
    schema.load(cat_data)
    category = CategoryModel(cat_data['name'], cat_data['description'])
    category.save_to_db()
    return jsonify({'id': category.id,
                    'name': category.name,
                    'description': category.description}), 201