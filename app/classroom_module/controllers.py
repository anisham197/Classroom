from flask import Flask, flash, redirect, render_template, request, session, url_for, Blueprint
from flask_session import Session
from app.helpers import *
#from tempfile import gettempdir
from app import db
from app.classroom_module.models import Classroom, User_Classroom
from app.queries import *

import random
# Define the blueprint
classroom_mod = Blueprint('classroom', __name__, url_prefix='/classes' , static_folder = '../static', template_folder = '../templates/classes')

# define role 'student' as 1
CREATOR = 0
STUDENT = 1
COLLABORATOR = 2

TEACHER = 0

@classroom_mod.route("/index", methods=["GET", "POST"])
@login_required
def index():
    if request.method == "GET" :
        #TODO Check for existing classes
        return render_template("classes/classroom.html")

    if request.method == "POST" :
        if (getClassroomByCode(request.form["class_code"]) == None ) :
            return render_template("auth/no_access.html")
        user_class = User_Classroom( session["user_id"], request.form["class_code"], STUDENT)
        db.session.add(user_class)
        db.session.commit()
        #TODO ADD new Classes
        return render_template("classes/classroom.html")


@classroom_mod.route("/createclass", methods=["GET", "POST"])
@login_required
def createclass():

    user = getUserByUserID(session["user_id"])
    if  user.role != TEACHER :
        return render_template("auth/no_access.html")

    if request.method == "GET" :
        #check with db that code is unique
        invalid = True
        while(invalid):
            code = random.randint(10000, 99999)
            class1 = getClassroomByCode( code )
            if class1 == None :
                invalid = False

        session["class_code"] = code
        return render_template("classes/create_class.html", code=code)

    if request.method == "POST" :
        new_class = Classroom(session["class_code"], session["user_id"], request.form["class_name"], request.form["subject"], request.form["sub_code"], request.form["credits"],request.form["semester"],request.form["description"])
        db.session.add(new_class)
        user_class = User_Classroom( session["user_id"], session["class_code"], CREATOR)
        db.session.add(user_class)
        db.session.commit()

        return redirect(url_for("classroom.index"))
