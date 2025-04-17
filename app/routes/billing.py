from flask import Blueprint, jsonify, request
import pymysql
import os

billing_bp = Blueprint('billing', __name__)

# Database connection
def get_db_connection():
    return pymysql.connect(
        host=os.getenv('DB_HOST', 'your-db-host'),
        user=os.getenv('DB_USER', 'your-db-user'),
        password=os.getenv('DB_PASSWORD', 'your-db-password'),
        db=os.getenv('DB_NAME', 'returnsdb'),
        cursorclass=pymysql.cursors.DictCursor
    )

# GET: List returns pending billing
@billing_bp.route('/billing/pending', methods=['GET'])
def get_pending_returns():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM billing WHERE Billed IS NULL LIMIT 50")
            data = cursor.fetchall()
        conn.close()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# POST: Update return as billed
@billing_bp.route('/billing/complete', methods=['POST'])
def complete_billing():
    try:
        content = request.json
        conn = get_db_connection()
        with conn.cursor() as cursor:
            sql = """
            UPDATE billing
            SET Billed = 1, Billing_Amount = %s, Billing_Date = NOW(), Billing_Comments = %s
            WHERE Shipment_ID = %s
            """
            cursor.execute(sql, (
                content.get('Billing_Amount'),
                content.get('Billing_Comments'),
                content.get('Shipment_ID')
            ))
            conn.commit()
        conn.close()
        return jsonify({'message': 'Return billed successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
