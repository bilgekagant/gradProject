
### 4. Database Connection and Operations (`db.py`):
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def reset_database(app):
    with app.app_context():
        db.drop_all()
        db.create_all()

def initialize_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
