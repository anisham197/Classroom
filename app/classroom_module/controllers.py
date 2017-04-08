from flask import Flask, flash, redirect, render_template, request, session, url_for, Blueprint
from flask_session import Session
from app.helpers import *
#from tempfile import gettempdir
from app import db
import random
# Define the blueprint
classroom_mod = Blueprint('classroom', __name__, url_prefix='/classes' , static_folder = '../static', template_folder = '../templates/classes')

@classroom_mod.route("/index", methods=["GET", "POST"])
@login_required
def index():
    if request.method == "GET" :
        #Check for existing classes
        return render_template("classes/no_classroom.html")


@classroom_mod.route("/createclass", methods=["GET", "POST"])
@login_required
def createclass():
    if request.method == "GET" :
        #check with db that code is unique
        code = random.randint(10000, 99999)
        return render_template("classes/create_class.html", code=code)
    if request.method == "POST" :
        return render_template("classes/classroom.html")
