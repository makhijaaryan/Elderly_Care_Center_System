from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# class UserResident(db.Model, UserMixin):
#     # id=db.Column(db.Integer, primary_key=True)
#     id=db.Column(db.String(10), primary_key=True)
#     email=db.Column(db.String(150), unique=True)
#     password = db.Column(db.String(150))
#     name = db.Column(db.String(150))
#     contactNo = db.Column(db.String(10))
#     requests=db.relationship('Request')

# class Request(db.Model):
#     # id=db.Column(db.Integer, primary_key=True)
#     reqNo = db.Column(db.String(10),primary_key=True)
#     rId=db.Column(db.String(10), db.ForeignKey('UserResident.id'))
#     problem=db.Column(db.String(1000))
#     date=db.Column(db.DateTime(timezone=True), default=func.now())
#     status=db.Column(db.String(10), default="requested")


class Note(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    data=db.Column(db.String(10000))
    date=db.Column(db.DateTime(timezone=True), default=func.now())
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))


class Requests(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
    userRequest=db.Column(db.String(10000))
    date=db.Column(db.DateTime(timezone=True), default=func.now())
    status=db.Column(db.String(20), default="active")


class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    # id=db.Column(db.String(10), primary_key=True)
    email=db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    contactNo = db.Column(db.String(10))
    role=db.Column(db.String(10))
    notes=db.relationship('Note')
    requests=db.relationship('Requests')




