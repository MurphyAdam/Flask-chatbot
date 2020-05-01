# -*- coding: utf-8 -*-

from flask import (Flask, current_app, flash, 
    render_template, request, 
    redirect, url_for, jsonify)

from app.factory import is_empty, kill_html
from app.chatbot import chatbot
from app.private_bot import PrivateBot


title = "Lang & Code - Chatterbot"
private_bot = PrivateBot("Adam")




@chatbot.route("/", methods=["GET", "POST"])
def index():
    return render_template('chatterbot.html', title=title)


@chatbot.route('/chat', methods=['POST'])
def chat():
    try:
        _csrf_token = request.form.get("_csrf_token")
        message = request.form.get('message')
        if message and not is_empty(message):
            message = kill_html(message)
            response = private_bot.get_response(message).text
            return jsonify(
                category="is-primary",
                response=response, 
                sent=message)
        return jsonify(
            category="is-danger", 
            response="[Empty words]: You cannot send empty messages",
            sent=None)
    except Exception as e:
        print(e)
        return jsonify(
            category="is-danger", 
            response="Sorry, but I think you have entered something I think is invalid or malicious",
            sent=None)