from flask import Blueprint, jsonify, request
import pymysql
import os

hub_bp = Blueprint('hub', __name__)

# Database connection
def get_db_connection():
    return pymysql.connect(
        host=os.getenv('DB_HOST', 'your-db-host'),
        user=os.getenv('DB_USER', 'your-db-user'),
        password=os.getenv('DB_PASSWORD', 'your-db-password'),
        db=os.getenv('DB_NAME', 'returnsdb'),
        cursorclass=pymysql.cursors.DictCursor
    )

# GET: List all hub-related return records
@hub_bp.route('/hub/returns', methods=['GET'])
def get_hub_returns():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM hub_returns LIMIT 50")
            data = cursor.fetchall()
        conn.close()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# POST: Update a return as booked back or damaged
@hub_bp.route('/hub/update', methods=['POST'])
def update_hub_return():
    try:
        content = request.json
        conn = get_db_connection()
        with conn.cursor() as cursor:
            sql = """
            UPDATE hub_returns
            SET Booked_Back = %s, Damaged = %s, Hub_Comments = %s
            WHERE Shipment_ID = %s
            """
            cursor.execute(sql, (
                content.get('Booked_Back'),
                content.get('Damaged'),
                content.get('Hub_Comments'),
                content.get('Shipment_ID')
            ))
            conn.commit()
        conn.close()
        return jsonify({'message': 'Hub return updated'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
