from flask import Flask, redirect, url_for, render_template, request, flash, session
from flask.helpers import send_from_directory
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


#####################
#   Error Routes
#####################
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', h1="ERROR 404", h2="Page not found"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', h1="ERROR 500", h2="internal Server Error"), 500

@app.errorhandler(403)
def page_forbidden(e):
    return render_template('error.html', h1="ERROR 403", h2="Page forbidden"), 403


@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('assets', path)