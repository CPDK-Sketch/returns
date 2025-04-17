# app/__init__.py

from flask import Flask
from app.routes import returns_bp, hub_bp, billing_bp, auth_bp

def create_app():
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(returns_bp)
   # app.register_blueprint(home_bp) 
    app.register_blueprint(hub_bp)
    app.register_blueprint(billing_bp)
    app.register_blueprint(auth_bp)

    return app
