from flask import Blueprint
from .routes import configure_routes

api_blueprint = Blueprint('api', __name__)
configure_routes(api_blueprint)
