from flask import Flask, flash, redirect, render_template, request, session, url_for, Blueprint
from flask_session import Session
from app.helpers import *
#from tempfile import gettempdir
from app import db

# Define the blueprint
classroom_mod = Blueprint('classroom', __name__, url_prefix='/classes' , static_folder = '../static', template_folder = '../templates/classroom')

@classroom_mod.route("/classroom", methods=["GET", "POST"])
@login_required
def classroom():
	return render_template("classes/classroom.html")
