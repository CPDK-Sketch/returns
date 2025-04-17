from flask import Blueprint, request, jsonify, render_template

returns_bp = Blueprint('/', __name__)

@returns_bp.route('/', methods=['GET', 'POST'])
def handle_returns():
    if request.method == 'POST':
        order_id = request.form.get('order_id')
        return_reason = request.form.get('return_reason')
        return_status = request.form.get('return_status')
        returned_to_hub = request.form.get('returned_to_hub')

        # 🧪 TODO: Store these values in DB if needed here.

        return f"<h2>Return submitted for Order ID: {order_id}</h2>"

    return render_template('returns_form.html')
