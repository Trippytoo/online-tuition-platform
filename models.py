from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy 

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)


class Category(db.Model):
    __tablename__ = "my_categories"
    id = db.Column(db.integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.TIMESTAMP)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)


class TutorProfile(db.Model):
    __tablename__ = "Tutor"
    id = db.Column(db.integer, primary_key=True)
    name = db.Column(db.text, nullable=False)

class Lesson(db.Model):
    __tablename__ = "Lessons"
    id = db.Column(db.integer, primary_key=True)
    name = db.Column(db.text, nullable=False)

class Review(db.Model):
    __tablename__ = "Review"
    id = db.Column(db.integer, primary_key=True)
    name = db.Column(db.text, nullable=False)


