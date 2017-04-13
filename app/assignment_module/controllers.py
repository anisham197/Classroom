from flask import Flask, flash, redirect, render_template, request, session, url_for, Blueprint
from flask_session import Session
from app.helpers import *
#from tempfile import gettempdir
from app import db
from app.queries import *

# Define the blueprint
assignment_mod = Blueprint('assignment', __name__, url_prefix='/assignments' , static_folder = '../static', template_folder = '../templates/assignments')

TEACHER = 0

@assignment_mod.route("/assign", methods=["GET", "POST"])
@login_required
def assign():
    # if request.method == "GET" :
    #     user = getUserByUserID(session["user_id"])
    #TODO check role of user for that particular classroom, and pass as parameter

    #TODO retrieve assignments for particular classroom, and pass as parameter

    return render_template("assignments/inside_class.html", role=0, assignments=None)

@assignment_mod.route("/createassign", methods=["GET", "POST"])
@login_required
def createassign():

    # user = getUserByUserID(session["user_id"])
    # if  user.role != TEACHER :
    #     return render_template("auth/no_access.html", msg="You do not have access to this page !")

    #TODO check role of user for that particular classroom, if not creator then display no_access

    if request.method == "GET" :
        return render_template("assignments/create_assignment.html")

    if request.method == "POST" :
        #TODO Write Assignment to database and commit
        return redirect(url_for("assignment.assign"))
