from flask import Blueprint, jsonify, request
import pymysql
import os

# Create Blueprint
returns_bp = Blueprint('returns', __name__)

# Database connection function
def get_db_connection():
    return pymysql.connect(
        host=os.getenv('DB_HOST', 'returnsdb.cx46s84o832r.eu-west-2.rds.amazonaws.com'),
        user=os.getenv('DB_USER', 'admin'),
        password=os.getenv('DB_PASSWORD', 'Huboo123456789'),
        db=os.getenv('DB_NAME', 'returns_table'),
        cursorclass=pymysql.cursors.DictCursor
    )

# Sample GET route to fetch all return records
@returns_bp.route('/returns', methods=['GET'])
def get_returns():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM returns_table LIMIT 50")
            data = cursor.fetchall()
        conn.close()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Sample POST route to insert a return record
@returns_bp.route('/returns', methods=['POST'])
def add_return():
    try:
        content = request.json
        conn = get_db_connection()
        with conn.cursor() as cursor:
            sql = """
            INSERT INTO returns_table (Order_ID, Return_Date, Return_Reason, Return_Status)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (
                content.get('Order_ID'),
                content.get('Return_Date'),
                content.get('Return_Reason'),
                content.get('Return_Status')
            ))
            conn.commit()
        conn.close()
        return jsonify({'message': 'Return record added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
from flask import Blueprint, request, jsonify
import pymysql
from app.config import Config

bp = Blueprint('returns', __name__, url_prefix='/returns')

@bp.route('/fetch', methods=['GET'])
def fetch_returns():
    try:
        connection = pymysql.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM returns_data LIMIT 10;")
        result = cursor.fetchall()
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)})
