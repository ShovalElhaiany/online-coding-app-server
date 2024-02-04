from src.extensions import socketio
from src import create_app
from src.data_manage import trigger_load_data

# Creating the Flask application instance using the create_app function
app = create_app()

# Triggering the loading of data using the trigger_load_data function
trigger_load_data()

# Importing views from the src.views module
from src.views import *

if __name__ == "__main__":
    # Running the Flask application with the socketio extension
    socketio.run(app, host="0.0.0.0", port=5000, debug=True, allow_unsafe_werkzeug=True)
