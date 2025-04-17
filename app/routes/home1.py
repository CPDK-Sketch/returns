from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def dashboard():
    return "<h1>Welcome to the Returns Management Tool</h1><p>Select a department from the menu.</p>"
