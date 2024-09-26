from flask import Blueprint, request, jsonify
from models import db, ShoeDetail, ShoeCategory

shoes_bp = Blueprint('shoes', __name__)

@shoes_bp.route('/api/shoes', methods=['POST'])
def add_shoe_detail():
    data = request.json
    # Pengecekan apakah category_id ada di tabel ShoeCategory
    category = ShoeCategory.query.get(data['category_id'])
    if not category:
        return jsonify({'message': 'Category ID does not exist'}), 400
    
    new_shoe = ShoeDetail(
        category_id=data['category_id'],
        shoe_name=data['shoe_name'],
        shoe_price=data['shoe_price'],
        shoe_size=data['shoe_size'],
        stock=data['stock']
    )
    db.session.add(new_shoe)
    db.session.commit()
    return jsonify({'message': 'Shoe detail added successfully'}), 201

@shoes_bp.route('/api/shoes/<int:shoe_detail_id>', methods=['PUT'])
def update_shoe_detail(shoe_detail_id):
    data = request.json
    shoe = ShoeDetail.query.get(shoe_detail_id)
    if not shoe:
        return jsonify({'message': 'Shoe detail not found'}), 404
    
    # Pengecekan apakah category_id ada di tabel ShoeCategory
    if 'category_id' in data:
        category = ShoeCategory.query.get(data['category_id'])
        if not category:
            return jsonify({'message': 'Category ID does not exist'}), 400
        shoe.category_id = data['category_id']
    
    shoe.shoe_name = data.get('shoe_name', shoe.shoe_name)
    shoe.shoe_price = data.get('shoe_price', shoe.shoe_price)
    shoe.shoe_size = data.get('shoe_size', shoe.shoe_size)
    shoe.stock = data.get('stock', shoe.stock)
    
    db.session.commit()
    return jsonify({'message': 'Shoe detail updated successfully'}), 200

@shoes_bp.route('/api/shoes/<int:shoe_detail_id>', methods=['DELETE'])
def delete_shoe_detail(shoe_detail_id):
    shoe = ShoeDetail.query.get(shoe_detail_id)
    if shoe:
        db.session.delete(shoe)
        db.session.commit()
        return jsonify({'message': 'Shoe detail deleted successfully'}), 200
    return jsonify({'message': 'Shoe detail not found'}), 404

@shoes_bp.route('/api/shoes/<int:shoe_detail_id>', methods=['GET'])
def get_shoe_detail(shoe_detail_id):
    shoe = ShoeDetail.query.get(shoe_detail_id)
    if shoe:
        return jsonify({
            'category_id': shoe.category_id,
            'shoe_name': shoe.shoe_name,
            'shoe_price': shoe.shoe_price,
            'shoe_size': shoe.shoe_size,
            'stock': shoe.stock
        }), 200
    return jsonify({'message': 'Shoe detail not found'}), 404

@shoes_bp.route('/api/shoes', methods=['GET'])
def get_all_shoes():
    shoes = ShoeDetail.query.all()
    result = []
    for shoe in shoes:
        result.append({
            'category_id': shoe.category_id,
            'shoe_name': shoe.shoe_name,
            'shoe_price': shoe.shoe_price,
            'shoe_size': shoe.shoe_size,
            'stock': shoe.stock
        })
    return jsonify({'message':'No Shoe detail found'}), 200
