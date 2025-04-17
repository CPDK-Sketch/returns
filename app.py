# app.py
from flask import Flask
from flask_cors import CORS
from routes.returns import returns_bp

app = Flask(__name__)
CORS(app)  # allows frontend (Vue) to access this API

# Register the route
app.register_blueprint(returns_bp)

@app.route('/')
def home():
    return 'Returns API is live!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

