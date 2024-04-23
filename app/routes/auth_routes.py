# app/routes/auth_routes.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user
from app.models.user import User
from app.utils.auth import register_user, get_user_by_username, get_user_by_email, verify_password
from flask_login import LoginManager, UserMixin


# Set auth blueprint
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # Check if the username or email already exists
        if get_user_by_username(username):
            flash('Username already exists. Please choose a different one.')
        elif get_user_by_email(email):
            flash('Email already exists. Please use a different one.')
        else:
            # Register the user if username and email are unique
            user = register_user(username, email, password)
            flash('Registration successful! Please log in.')
            return redirect(url_for('auth.login'))
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = get_user_by_username(username)
        if user and verify_password(user, password):
            login_user(user)
            flash('Login successful!')
            return redirect(url_for('homepage.login_success'))
        else:
            flash('Invalid username or password.')
    return render_template('login.html')

# @auth_bp.route('/logout')
# def logout():
#     logout_user()
#     flash('You have been logged out.')
#     return redirect(url_for('homepage.index'))
