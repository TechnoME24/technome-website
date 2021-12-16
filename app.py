import time
from flask import Flask, redirect, url_for, render_template, request, flash, session
from flask.helpers import send_from_directory
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(hours=1)


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


#####################
#   Website routes
#####################

@app.route('/', methods=["POST","GET"])
def index():
    if request.method == "POST":
        if 'username' in request.form:
            session['user'] = request.form['username']
            return redirect(url_for('index'))
    else:
        return render_template('index.html')

@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for('index'))


#####################
#   Backend routes
#####################

@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('assets', path)

if __name__ == "__main__":
	app.run(debug=True)