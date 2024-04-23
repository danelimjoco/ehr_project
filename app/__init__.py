from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize Flask extensions
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config['SECRET_KEY'] = 'your_secret_key_here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://danelimjoco:Uppt1986!@db:5432/ehr_database'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from app.models.user import User  # Import inside the function
        return User.query.get(int(user_id))

    # Register blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.homepage_routes import homepage_bp
    from app.routes.patient_routes import patient_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(homepage_bp)
    app.register_blueprint(patient_bp)

    return app
