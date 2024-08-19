from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

# Contact Model
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Contact {self.name}>"
