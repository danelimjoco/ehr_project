from flask import Blueprint, render_template

# Create a Blueprint for the homepage routes
homepage_bp = Blueprint('homepage', __name__)

# Define the route for the homepage
@homepage_bp.route('/')
def index():
    # Render the index.html template for the homepage
    return render_template('homepage.html')
