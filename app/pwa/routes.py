from flask import Blueprint, make_response, send_from_directory
from app.pwa import pwa








@pwa.route('/manifest.json')
def manifest():
    return send_from_directory('static', 'manifest.json')


@pwa.route('/sw.js')
def service_worker():
    response = make_response(send_from_directory('static', 'sw.js'))
    response.headers['Cache-Control'] = 'no-cache'
    return response
