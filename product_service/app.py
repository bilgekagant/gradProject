# product_service/app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/productdb'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define routes and models for product service here

if __name__ == '__main__':
    app.run(debug=True, port=5001)
