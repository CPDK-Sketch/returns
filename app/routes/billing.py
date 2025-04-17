# app/routes/billing.py

from flask import Blueprint, jsonify

billing_bp = Blueprint('billing', __name__)

@billing_bp.route('/billing', methods=['GET'])
def billing_home():
    return jsonify({'message': 'Billing route working'})
