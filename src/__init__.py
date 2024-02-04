from .extensions import app, db, cors, socketio
from .config import Config


# Function to create the database tables
def create_database():
    with app.app_context():
        db.create_all()


# Function to create and configure the Flask application
def create_app():
    # Configuring the app using the Config class
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    cors.init_app(app)
    socketio.init_app(app)

    # Creating the database tables
    create_database()

    # Pushing the app context to ensure proper functioning
    app.app_context().push()

    return app
