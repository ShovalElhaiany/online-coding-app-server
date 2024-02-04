# Create a virtual environment named .venv
py -m venv .venv

# Activate the virtual environment
.venv/scripts/activate

# Upgrade pip within the virtual environment
python.exe -m pip install --upgrade pip

# Install Python dependencies specified in requirements.txt
pip install -r requirements.txt

# Run the server application
python app.py
