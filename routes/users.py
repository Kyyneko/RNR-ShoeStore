from flask import Blueprint, request, jsonify
from models import db, User

users_bp = Blueprint('users', __name__)

@users_bp.route('/api/users/register', methods=['POST'])
def register():
    data = request.json

    existing_user = User.query.filter_by(username=data['username']).first()
    if existing_user:
        return jsonify({'message': 'Username already exists'}), 409
    
    new_user = User(
        username=data['username'],
        password=data['password'],
        email=data['email'],
        first_name=data.get('first_name'),  
        last_name=data.get('last_name'),   
        address=data.get('address'),
        phone=data.get('phone'),
        role=data.get('role', 'User')
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@users_bp.route('/api/users/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username'], password=data['password']).first()
    if user:
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@users_bp.route('/api/users/profile/<int:user_id>', methods=['PUT'])
def update_profile(user_id):
    data = request.json
    user = User.query.get(user_id)
    if user:
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        user.first_name = data.get('first_name', user.first_name) 
        user.last_name = data.get('last_name', user.last_name)  
        user.address = data.get('address', user.address)
        user.phone = data.get('phone', user.phone)
        db.session.commit()
        return jsonify({'message': 'Profile updated successfully'}), 200
    return jsonify({'message': 'User not found'}), 404

@users_bp.route('/api/users/logout', methods=['POST'])
def logout():
    # Logout logic (e.g., clear session) goes here
    return jsonify({'message': 'Logged out successfully'}), 200

@users_bp.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({
            'user_id': user.user_id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,  
            'last_name': user.last_name,   
            'address': user.address,
            'phone': user.phone,
            'role': user.role
        }), 200
    return jsonify({'message': 'User not found'}), 404

@users_bp.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    if users:
        result = []
        for user in users:
            result.append({
                'user_id': user.user_id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,  
                'last_name': user.last_name,  
                'address': user.address,
                'phone': user.phone,
                'role': user.role
            })
        return jsonify(result), 200
    return jsonify({'message': 'No Users found'}), 404


@users_bp.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 200
    return jsonify({'message': 'User not found'}), 404
