# app/routes/auth.py

from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    # Replace with real DB check later
    if username == 'admin' and password == 'password':
        return jsonify({'message': 'Login successful', 'role': 'admin'})
    return jsonify({'message': 'Invalid credentials'}), 401
