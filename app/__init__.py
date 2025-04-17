def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(returns_bp)
    app.register_blueprint(hub_bp)
    app.register_blueprint(billing_bp)
    app.register_blueprint(auth_bp)
    
    return app
