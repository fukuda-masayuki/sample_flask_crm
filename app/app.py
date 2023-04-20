from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class CTest(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Integer)

@app.route("/")
def index():
    return "testh"


if __name__ == "__main__":
    app.run(debug=True)