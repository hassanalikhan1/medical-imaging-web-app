from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
print(app)
CORS(app)  # Enable CORS if needed

# Import routes and other modules
from backend import routes
