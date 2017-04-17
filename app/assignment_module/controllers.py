from flask import Flask, flash, redirect, render_template, request, session, url_for, Blueprint
from flask_session import Session
from app.helpers import *
#from tempfile import gettempdir
from app import db
from app.assignment_module.models import Assignment
from app.queries import *

# Define the blueprint
assignment_mod = Blueprint('assignment', __name__, url_prefix='/assignments' , static_folder = '../static', template_folder = '../templates/assignments')

STUDENT = 1
class_code = None

@assignment_mod.route("/assign", methods=["GET"])
@login_required
def assign():
    if request.method == "GET" :
        user = getUserByUserID(session["user_id"])
        # global class_code
        session["class_code"] = request.args.get('class_code')
        # Get role of the user for the selected class
        role = getUser_ClassroomByCodeAndID(session["user_id"], session["class_code"]).role

        print("\n\n role " + str(role) + "\n\n")
        print("\nclass_code " + str(class_code) + "\n\n")

        assignments = getAssignmentByClassCode(session["class_code"])
        # TODO : Remove count later
        print ("\n\n\n\nsession " +session["class_code"])
        print(assignments)
        count = x(session["class_code"])
        print("\n\ncount " + str(count))

        for assignment in assignments :
            print("\n\n title " + assignment.title)
        print("\n\n done\n\n")
        return render_template("assignments/inside_class.html", role=role, assignments=assignments)

@assignment_mod.route("/createassign", methods=["GET", "POST"])
@login_required
def createassign():

    role = getUser_ClassroomByCodeAndID(session["user_id"], session["class_code"]).role
    if role == STUDENT :
        return render_template("auth/no_access.html", msg="You do not have access to this page !")

    # class_code = request.args.get('class_code')
    #global class_code
    # TODO : check if it is necessary to validate class code

    # if class_code == None :
    #     return render_template("auth/no_access.html", msg="ERROR!! Class code is null!")

    print("\n\n class_code create assign " + str(session["class_code"]) + "\n\n")

    if request.method == "GET" :
        return render_template("assignments/create_assignment.html")

    if request.method == "POST" :
        doc_file = pdf_file = ppt_file = zip_file = 1
        if request.form.get('doc_file') == None :
            doc_file = 0
        if request.form.get('pdf_file') == None :
            pdf_file = 0
        if request.form.get('ppt_file') == None :
            ppt_file = 0
        if request.form.get('zip_file') == None :
            zip_file = 0
        # print("\n\n class_code " + str(class_code) + "\ntitle " + request.form["title"] + "\ndate " + request.form["last_date"] + "\ndoc " + request.form.get('doc_file') + "\n\n")
        new_assignment = Assignment(session["class_code"], request.form["title"], request.form["last_date"] , request.form["max_score"], request.form["description"], doc_file, pdf_file, ppt_file, zip_file)
        db.session.add(new_assignment)
        db.session.commit()
        return redirect(url_for("assignment.assign", class_code=session["class_code"]))

@assignment_mod.route("/openassign", methods=["GET", "POST"])
@login_required
def openassign():
    return render_template("assignments/view_assignment.html", role=0, assignments=None)
