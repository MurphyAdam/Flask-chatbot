from flask import Blueprint
pwa = Blueprint('pwa', __name__)
from app.pwa import routes
