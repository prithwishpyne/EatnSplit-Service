from db import db
from sqlalchemy_serializer import SerializerMixin

class UserMaster(db.Model, SerializerMixin):
    __tablename__ = "user_master"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(400))
    balance = db.Column(db.Integer)
    image = db.Column(db.String(400))
    is_active = db.Column(db.String(400))
    created_datetime = db.Column(db.DateTime)