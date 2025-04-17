# app/routes/hub.py

from flask import Blueprint, jsonify

hub_bp = Blueprint('hub', __name__)

@hub_bp.route('/hub', methods=['GET'])
def hub_dashboard():
    return jsonify({'message': 'Hub team route working'})
