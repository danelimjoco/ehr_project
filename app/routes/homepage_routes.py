from flask import Blueprint, render_template, redirect, url_for

# Create a Blueprint for the homepage routes
homepage_bp = Blueprint('homepage', __name__)

# Define the route for the homepage
@homepage_bp.route('/')
def index():
    return redirect(url_for('auth.login'))

@homepage_bp.route('/homepage')
def login_success():
    return render_template('homepage.html')

