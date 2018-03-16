from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:zszl15143121@127.0.0.1:3306/filesystem"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = True

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    pwd = db.Column(db.String(100), nullable=False)
    addtime = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<User %r>" % self.name


class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    category = db.Column(db.Integer, nullable=False)
    author = db.Column(db.Integer, nullable=False)
    cover = db.Column(db.Integer, unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    addtime = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<Article %r>" % self.title


if __name__ == "__main__":
    db.create_all()
