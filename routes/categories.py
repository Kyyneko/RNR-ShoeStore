from flask import Blueprint, request, jsonify
from models import db, ShoeCategory

categories_bp = Blueprint('categories', __name__)

@categories_bp.route('/api/categories', methods=['POST'])
def add_category():
    data = request.json
    new_category = ShoeCategory(category_name=data['category_name'])
    db.session.add(new_category)
    db.session.commit()
    return jsonify({'message': 'Category added successfully'}), 201

@categories_bp.route('/api/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    category = ShoeCategory.query.get(category_id)
    if category:
        db.session.delete(category)
        db.session.commit()
        return jsonify({'message': 'Category deleted successfully'}), 200
    return jsonify({'message': 'Category not found'}), 404

@categories_bp.route('/api/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    data = request.json
    category = ShoeCategory.query.get(category_id)
    if category:
        category.category_name = data.get('category_name', category.category_name)
        db.session.commit()
        return jsonify({'message': 'Category updated successfully'}), 200
    return jsonify({'message': 'Category not found'}), 404

@categories_bp.route('/api/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    category = ShoeCategory.query.get(category_id)
    if category:
        return jsonify({
            'category_id': category.category_id,
            'category_name': category.category_name
        }), 200
    return jsonify({'message': 'Category not found'}), 404

@categories_bp.route('/api/categories', methods=['GET'])
def get_categories():
    categories = ShoeCategory.query.all()
    if categories:
        result = []
        for category in categories:
            result.append({
                'category_id': category.category_id,
                'category_name': category.category_name
            })
        return jsonify(result), 200
    return jsonify({'message': 'No categories found'}), 404
