from flask import Flask, flash, redirect, render_template, request, session, url_for, Blueprint
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import gettempdir

from app.auth_module.helpers import *
# from models.users import *
from app import db

# Import module models (i.e. User)
from app.auth_module.models import User, Student

auth_mod = Blueprint('auth', __name__, url_prefix='/auth' , static_folder = '../static', template_folder = '../templates/auth')

@auth_mod.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""

    # forget any user_id
    session.clear()

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # query database for username
        user = User.query.filter(User.username == request.form.get("username")).first()

        # ensure username exists and password is correct
        if user == None or not pwd_context.verify(request.form.get("password"), user.password):
            flash("Invalid Username/Password !", 'error')
            return render_template("auth/login.html")

        # remember which user has logged in
        session["user_id"] = user.id

        # redirect user to home page
        flash("You are logged in !", 'info')
        return render_template("auth/login.html")

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("auth/login.html")

@auth_mod.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST" :
        user = User.query.filter( User.username == request.form.get("username") ) .first()
        student = Student.query.filter(  (Student.usn == request.form.get("usn")) ).first()

        if user != None:
            flash("Username already exists !", 'error')
            return render_template("auth/signup.html")

        if  student != None:
            flash("USN already exists !", 'error')
            return render_template("auth/signup.html")

        if request.form["password"] != request.form["c_password"] :
            flash("Passwords don't match !", 'error')
            return render_template("auth/signup.html")

        user = User(request.form["username"], pwd_context.encrypt(request.form["password"]), 1 )
        db.session.add(user)
        db.session.commit()

        user = User.query.filter(User.username == request.form.get("username")).first()
        student = Student(user.id, request.form["name"], request.form["usn"], request.form["branch"], request.form["email"])
        db.session.add(student)
        db.session.commit()
        #store details in table
        flash("You have successfully Signed Up !", 'info')
        return render_template("auth/login.html")

    # else if user reached route via GET (as by clicking a link or via redirect)
    else :
        return render_template("auth/signup.html")
