from flask import request, jsonify
from . import api
from app.models.category import CategoryModel
from app.models.item import ItemModel
from app.models.user import UserModel
from flask_jwt import jwt_required, current_identity
from app.schemas.item import ItemSchema
from app import db

@api.route('/categories/<int:category_id>/items', methods=['GET'])
def get_items(category_id):
    category = CategoryModel.query.get_or_404(category_id)
    return jsonify({'items': [item.export_data() for item in
                                    category.items.all()]})

@api.route('/categories/<int:category_id>/items', methods=['POST'])
@jwt_required()
def new_item(category_id):
    item_data = request.json
    if item_data:
        item_data['category_id'] = category_id
        item_data['user_id'] = current_identity.id
    category = CategoryModel.query.get_or_404(category_id)
    schema = ItemSchema()
    schema.load(item_data)
    item = ItemModel(item_data['name'], item_data['description'], item_data['price'], category_id, current_identity.id)
    item.save_to_db()
    return jsonify({'id': item.id,
                    'name': item.name,
                    'description': item.description,
                    'price': item.price,
                    'category_id': item.category_id,
                    'user_id': item.user_id}), 201

@api.route('/categories/<int:category_id>/items/<int:item_id>', methods=['GET'])
def get_item(category_id, item_id):
    item = ItemModel.query.get_or_404(item_id)
    if item.category_id == category_id:
        return jsonify(item.export_data())
    else:
        return "Item not found", 404

@api.route('/categories/<int:category_id>/items/<int:item_id>', methods=['PUT'])
@jwt_required()
def update_item(category_id, item_id):
    item = ItemModel.query.get_or_404(item_id)
    if item.category_id == category_id :
        if item.user_id == current_identity.id:
            item_data = request.json
            if item_data:
                item_data['category_id'] = category_id
                item_data['user_id'] = current_identity.id
            schema = ItemSchema()
            schema.load(item_data)
            item.import_data(item_data)
            item.save_to_db()
            return jsonify(item.export_data())
        else:
            return "Not authorized", 401
    else:
        return "Item not found", 404

@api.route('/categories/<int:category_id>/items/<int:item_id>', methods=['DELETE'])
@jwt_required()
def delete_item(category_id, item_id):
    item = ItemModel.query.get_or_404(item_id)
    if item.category_id == category_id :
        if item.user_id == current_identity.id:
            db.session.delete(item)
            db.session.commit()
            return jsonify({}), 200
        else:
            return "Not authorized", 401
    else:
        return "Item not found", 404