from flask import Flask, render_template, request, redirect, url_for
from models import db, Contact

app = Flask(__name__)
app.secret_key = "your_secret_key"


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

# Create the database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')

    new_contact = Contact(name=name, phone=phone, email=email)
    db.session.add(new_contact)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/delete_contact/<int:id>')
def delete_contact(id):
    contact = Contact.query.get(id)
    if contact:
        db.session.delete(contact)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
