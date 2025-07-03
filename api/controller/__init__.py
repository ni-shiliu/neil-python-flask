from flask import Blueprint
from libs.external_api import ExternalApi


bp = Blueprint("neil", __name__, url_prefix="/api")
api = ExternalApi(bp)

from . import user_controller
