from .extensions import db


# Defining the CodeBlock model that represents a code snippet in the database
class CodeBlock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    code = db.Column(db.Text, nullable=False)

    # Method to convert the CodeBlock instance to a dictionary for easy serialization
    def as_dict(self):
        return {"id": self.id, "title": self.title, "code": self.code}


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Boolean column to indicate whether the user is a mentor or not
    mentor = db.Column(db.Boolean, default=False)
