from .models import CodeBlock, User
from .extensions import db
import json
import os


# Create and insert CodeBlock objects
def load_data():
    # Load JSON file
    with open("code_blocks.json", "r") as file:
        code_blocks_data = json.load(file)

    for block_data in code_blocks_data:
        code_block = CodeBlock(title=block_data["title"], code=block_data["code"])
        db.session.add(code_block)
    db.session.commit()

    existing_user = User.query.first()
    if not existing_user:
        new_user = User(mentor=True)
        db.session.add(new_user)
        db.session.commit()


# Function to check if the lock file exists
def is_lock_file_exists():
    return os.path.exists("lock.txt")


# Function to create the lock file
def create_lock_file():
    with open("lock.txt", "w") as lock_file:
        lock_file.write("locked")


# trigger data loading
def trigger_load_data():
    if not is_lock_file_exists():
        load_data()
        create_lock_file()
