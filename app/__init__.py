# __init__.py

import psycopg2
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():

    # Create the Flask app
    app = Flask(__name__)

	# Set logger level
    app.logger.setLevel(logging.INFO) 

    # Database configuration for SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://danelimjoco:Uppt1986!@db:5432/ehr_database'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize SQLAlchemy within the app
    db.init_app(app)

    # Register homepage blueprint
    from .routes.homepage_routes import homepage_bp
    app.register_blueprint(homepage_bp)


    # Register patient blueprint
    from .routes.patient_routes import patient_bp
    app.register_blueprint(patient_bp)
    

    return app