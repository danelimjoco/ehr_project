# app/utils/auth.py

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app.models.user import User
from app import db

def hash_password(password):
    return generate_password_hash(password)

def verify_password(user, password):
    return check_password_hash(user.password_hash, password)

def register_user(username, email, password):
    user = User(username=username, email=email, password_hash=hash_password(password))
    db.session.add(user)
    db.session.commit()
    return user

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()
