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
        # Check for existing classes
        role = getUserByUserID(session["user_id"]).role
        joined_classes = getJoinedClassroom(session["user_id"], db.session)
        created_classes = getCreatedClassroom(session["user_id"], db.session)
        if role == 1 :
            return render_template("classes/main_class.html", role=role, classes=joined_classes)
        else :
            return render_template("classes/main_class.html", role=role, classes=created_classes)

    if request.method == "POST" :
        # Check whether the entered class code is valid
        if (getClassroomByCode(request.form["class_code"]) == None ) :
            return render_template("auth/no_access.html", msg="Incorrect Class Code")

        # Check whether student is already a part of the classroom
        user_class = getUser_ClassroomByCodeAndID(session["user_id"],request.form["class_code"])
        if (user_class != None):
            if user_class.role == STUDENT :
                return render_template("auth/no_access.html", msg="Already part of this class")
            else :
                return render_template("auth/no_access.html", msg="You are creator of this class")

        # Add the student to the classroom
        user_class = User_Classroom( session["user_id"], request.form["class_code"], STUDENT)
        db.session.add(user_class)
        db.session.commit()
        return redirect(url_for("classroom.index"))

@classroom_mod.route("/joined_classes", methods=["GET", "POST"])
@login_required
def joined_classes():
    if request.method == "GET" :
        # Check for existing classes
        role = getUserByUserID(session["user_id"]).role
        joined_classes = getJoinedClassroom(session["user_id"], db.session)
        if role == 0 :
            return render_template("classes/main_class.html", role=  role, classes=joined_classes)

@classroom_mod.route("/createclass", methods=["GET", "POST"])
@login_required
def createclass():
    user = getUserByUserID(session["user_id"])
    # Only teachers can create class
    if  user.role != TEACHER :
        return render_template("auth/no_access.html",msg="You do not have access to this page !")

    if request.method == "GET" :
        #check with db that code is unique
        invalid = True
        while(invalid):
            code = random.randint(10000, 99999)
            if getClassroomByCode(code) == None :
                invalid = False

        session["join_code"] = code
        return render_template("classes/create_class.html", code=code)

    if request.method == "POST" :
        new_class = Classroom(session["join_code"], session["user_id"], request.form["class_name"], request.form["subject"], request.form["sub_code"], request.form["credits"],request.form["semester"],request.form["description"])
        db.session.add(new_class)
        db.session.commit()
        user_class = User_Classroom( session["user_id"], session["join_code"], CREATOR)
        db.session.add(user_class)
        db.session.commit()

        return redirect(url_for("classroom.index"))

@classroom_mod.route("/leaveclass", methods=["GET", "POST"])
@login_required
def leaveclass():
    user_classroom = getUser_ClassroomByCodeAndID(session['user_id'], session['class_code'])
    db.session.delete(user_classroom)
    db.session.commit()
    return redirect(url_for("classroom.index"))

@classroom_mod.route("/deleteclass", methods=["GET", "POST"])
@login_required
def deleteclass():
    role = getUser_ClassroomByCodeAndID(session["user_id"], session["class_code"]).role
    # Only creators can delete class
    if  role != CREATOR :
        return render_template("auth/no_access.html", msg="You do not have access to this page !")

    else :
        classroom = getClassroomByCode(session['class_code'])
        db.session.delete(classroom)
        db.session.commit()
        return redirect(url_for("classroom.index"))
