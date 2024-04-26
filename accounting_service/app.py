# accounting_service/app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .api.routes import api
from .models.user import User  # Ensure all models are imported to register them with SQLAlchemy
from flask_migrate import Migrate

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:4525se4525@localhost/gradProject'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize plugins
    db = SQLAlchemy(app)

    db.init_app(app)
    Migrate(app, db)

    # Register blueprints
    app.register_blueprint(api, url_prefix='/api')

    @app.route('/')
    def home():
        return "Welcome to the Accounting Service!"

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)