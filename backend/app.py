from flask import Flask
from flask_cors import CORS
from app.routes import routes_blueprint

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000", "methods": ["GET", "POST", "OPTIONS"]}})

# Register the routes Blueprint
app.register_blueprint(routes_blueprint, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)
