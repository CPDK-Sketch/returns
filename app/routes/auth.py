from flask import Blueprint, request, jsonify
import pymysql
import os

auth_bp = Blueprint('auth', __name__)

# DB connection
def get_db_connection():
    return pymysql.connect(
        host=os.getenv('DB_HOST', 'your-db-host'),
        user=os.getenv('DB_USER', 'your-db-user'),
        password=os.getenv('DB_PASSWORD', 'your-db-password'),
        db=os.getenv('DB_NAME', 'returnsdb'),
        cursorclass=pymysql.cursors.DictCursor
    )

# Login route
@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        conn = get_db_connection()
        with conn.cursor() as cursor:
            sql = "SELECT * FROM users WHERE username=%s AND password=%s AND active=1"
            cursor.execute(sql, (username, password))
            user = cursor.fetchone()
        conn.close()

        if user:
            return jsonify({'message': 'Login successful', 'role': user['role']}), 200
        else:
            return jsonify({'error': 'Invalid credentials or inactive user'}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Admin - Add new user
@auth_bp.route('/admin/add_user', methods=['POST'])
def add_user():
    try:
        data = request.json
        conn = get_db_connection()
        with conn.cursor() as cursor:
            sql = """
            INSERT INTO users (username, password, role, active)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (
                data.get('username'),
                data.get('password'),
                data.get('role'),
                data.get('active', 1)
            ))
            conn.commit()
        conn.close()
        return jsonify({'message': 'User added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
