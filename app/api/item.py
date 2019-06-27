from flask import request, jsonify
from . import api
from app.models.category import CategoryModel
from app.models.item import ItemModel
from app.models.user import UserModel

@api.route('/categories/<int:category_id>/items', methods=['GET'])
def get_items(category_id):
    category = CategoryModel.query.get_or_404(category_id)
    return jsonify({'items': [item.export for item in
                                    category.items.all()]})

@api.route('/categories/<int:category_id>/items', methods=['POST'])
def new_item(category_id):
    item_data = request.json
    category = CategoryModel.query.get_or_404(category_id)
    item = ItemModel(item_data['name'], item_data['description'], item_data['price'], category_id, 1)
    return jsonify({'id': item.id,
                    'name': item.name,
                    'description': item.description,
                    'price': item.price,
                    'category_id': item.category_id,
                    'user_id': item.user_id}), 201