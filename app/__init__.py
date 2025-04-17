from flask import Flask
from app.routes import returns, hub, billing, auth

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Register blueprints
    app.register_blueprint(returns.returns_bp)
    app.register_blueprint(hub.hub_bp)
    app.register_blueprint(billing.billing_bp)
    app.register_blueprint(auth.auth_bp)

    return app
