from flask import Flask
from flask_cors import CORS

if __name__ == '__main__':
    
    app = Flask(__name__)
    CORS(app)  # Enable CORS if needed
    
    app.run(debug=True)