from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    email = db.Column(db.String(100), index=True, unique=True)
    password_hash = db.Column(db.String(255))
    is_active = db.Column(db.Boolean, default=True)  

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def get_id(self):
        return str(self.user_id) 

    def serialize(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            'is_active': self.is_active,
        }
