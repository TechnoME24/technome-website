from flask import Flask, redirect, url_for, render_template, request, flash, Blueprint
from flask.helpers import send_from_directory

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=['GET', 'POST'])
def register():

    username = request.form.get('username')
    email = request.form.get('email')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')



    return render_template('register.html')

@auth.route("/login", methods=['GET','POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    return redirect(url_for("views.index"))

@auth.route("/logout")
def logout():
    return "logout"