from flask import Blueprint
chatbot = Blueprint('chatbot', __name__)
from app.chatbot import routes
