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
        user = getUserByUserID(session["user_id"])
        joined_classes = getJoinedClassroom(session["user_id"], db.session)
        created_classes = getCreatedClassroom(session["user_id"], db.session)
            # x =[]
            # for (class1 ,user_class) in user_classes :
            #     x.append(class1)
            #     print ("\n\nyayyaya\n" + str(user_class.user_id) + "\n\n " + class1.subject)
        return render_template("classes/main_class.html", role=user.role, joined_classes=joined_classes, created_classes=created_classes)


    if request.method == "POST" :
        # Check whether the entered class code is valid
        if (getClassroomByCode(request.form["class_code"]) == None ) :
            return render_template("auth/no_access.html", msg="Incorrect Class Code")

        # Check whether student is already a part of the classroom
        if (getUser_ClassroomByCodeAndID(session["user_id"],request.form["class_code"]) != None):
            return render_template("auth/no_access.html", msg="Already part of this class")

        # Add the student to the classroom
        user_class = User_Classroom( session["user_id"], request.form["class_code"], STUDENT)
        db.session.add(user_class)
        db.session.commit()
        return redirect(url_for("classroom.index"))


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
