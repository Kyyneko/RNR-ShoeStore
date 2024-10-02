from flask import Blueprint, request, jsonify
from models import db, SearchHistory, User  
from datetime import datetime, timedelta
import pytz

search_history_bp = Blueprint('search_history', __name__)

def get_current_time_wita():
    # Mengambil waktu saat ini di zona waktu WITA
    wita_tz = pytz.timezone('Asia/Makassar') 
    return datetime.now(wita_tz)

@search_history_bp.route('/api/search_history/<int:user_id>', methods=['GET'])
def get_search_history(user_id):
 
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    search_history = SearchHistory.query.filter_by(id_user=user_id).all()
    if search_history:
        result = []
        for search in search_history:
            result.append({
                'id_search': search.id_search,
                'id_user': search.id_user,
                'search_term': search.search_term,
                'date_searched': search.date_searched.isoformat()
            })
        return jsonify(result), 200
    return jsonify({'message': 'No search history found'}), 404

@search_history_bp.route('/api/search_history', methods=['POST'])
def add_search_history():
    data = request.json

    user = User.query.get(data['id_user'])
    if not user:
        return jsonify({'message': 'User not found'}), 404


    new_search = SearchHistory(
        id_user=data['id_user'],
        search_term=data['search_term'],
        date_searched=get_current_time_wita()
    )
    db.session.add(new_search)
    db.session.commit()
    return jsonify({'message': 'Search history added successfully'}), 201

@search_history_bp.route('/api/search_history/<int:id_search>', methods=['DELETE'])
def remove_search_history(id_search):
    search = SearchHistory.query.get(id_search)
    if search:
        db.session.delete(search)
        db.session.commit()
        return jsonify({'message': 'Search history removed successfully'}), 200
    return jsonify({'message': 'Search history not found'}), 404

@search_history_bp.route('/api/search_history/<int:id_search>', methods=['PUT'])
def update_search_history(id_search):
    data = request.json
    search = SearchHistory.query.get(id_search)
    if search:
        search.id_user = data.get('id_user', search.id_user)
        search.search_term = data.get('search_term', search.search_term)
        search.date_searched = get_current_time_wita()
          
        db.session.commit()
        return jsonify({'message': 'Search history updated successfully'}), 200
    return jsonify({'message': 'Search history not found'}), 404

@search_history_bp.route('/api/search_history/item/<int:id_search>', methods=['GET'])
def get_search_history_item(id_search):
    search = SearchHistory.query.get(id_search)
    if search:
        return jsonify({
            'id_search': search.id_search,
            'id_user': search.id_user,
            'search_term': search.search_term,
            'date_searched': search.date_searched.isoformat()
        }), 200
    return jsonify({'message': 'Search history not found'}), 404

@search_history_bp.route('/api/search_history', methods=['GET'])
def get_all_search_history():
    search_history = SearchHistory.query.all()
    result = []
    for search in search_history:
        result.append({
            'id_search': search.id_search,
            'id_user': search.id_user,
            'search_term': search.search_term,
            'date_searched': search.date_searched.isoformat()
        })
    return jsonify(result), 200
