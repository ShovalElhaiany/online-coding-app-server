# Import necessary modules from Flask and extensions
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_socketio import SocketIO

app: Flask = Flask(__name__)
db: SQLAlchemy = SQLAlchemy()
cors = CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")
