from flask import Blueprint
from flask_restful import Api

rest_bp = Blueprint('rest_bp', __name__, url_prefix='/rest')
api_rest = Api(rest_bp)
from .routers import *