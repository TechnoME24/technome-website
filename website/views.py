from flask import Flask, redirect, url_for, render_template, request, flash, session, Blueprint

views = Blueprint("views", __name__)

@views.route('/')
def index():
    return render_template('index.html')


#####################
#   Error Routes
#####################

def page_not_found(e):
    return render_template('error.html', h1="ERROR 404", h2="Page not found"), 404

def internal_server_error(e):
    return render_template('error.html', h1="ERROR 500", h2="internal Server Error"), 500

def page_forbidden(e):
    return render_template('error.html', h1="ERROR 403", h2="Page forbidden"), 403