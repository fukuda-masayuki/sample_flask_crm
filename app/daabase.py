from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
# sqliteを使うように設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlte:///test.db'
db = SQLAlchemy(app)

class Test(db.Model):
    __tablename__ = "test"
    id = Column(db.Integer,primary_key=True)
    name = Column(db.String(50),primary_key=True)


db = SQLAlchemy


db.create_all()

