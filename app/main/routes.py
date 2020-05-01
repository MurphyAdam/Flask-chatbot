# -*- coding: utf-8 -*-

from flask import current_app, make_response, render_template, flash, request, jsonify
from app.main import main



title = "ChatBot - Home"



##########################  APP CHATBOT ############################

if current_app.config["DEBUG"]:
    @main.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response


@main.route("/")
def index():
    return render_template("main/index.html", title=title)


@main.route("/hire_me")
def hire_me():
    title = "Lang & Code - Hire me"
    return render_template("hire_me.html", title=title)