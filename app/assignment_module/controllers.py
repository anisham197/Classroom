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
        assignments = getAssignmentByClassCode(session["class_code"])
        class_name = getClassroomByCode(session["class_code"]).class_name
        return render_template("assignments/inside_class.html",class_code=session["class_code"],class_name=class_name,role=role, assignments=assignments)

@assignment_mod.route("/createassign", methods=["GET", "POST"])
@login_required
def createassign():

    role = getUser_ClassroomByCodeAndID(session["user_id"], session["class_code"]).role
    if role == STUDENT :
        return render_template("auth/no_access.html", msg="You do not have access to this page !")

    if request.method == "GET" :
        return render_template("assignments/create_assignment.html", class_code=session["class_code"])

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

        if doc_file == 0 and pdf_file == 0 and ppt_file == 0 and zip_file == 0:
            doc_file = pdf_file = ppt_file = zip_file = 1
        new_assignment = Assignment(session["class_code"], request.form["title"], request.form["last_date"] , request.form["max_score"], request.form["description"], doc_file, pdf_file, ppt_file, zip_file)
        db.session.add(new_assignment)
        db.session.commit()
        return redirect(url_for("assignment.assign", class_code=session["class_code"]))

@assignment_mod.route("/viewassign", methods=["GET", "POST"])
@login_required
def viewassign():
    if request.method == "GET" :
        session["assignment_id"] = request.args.get('id')
        # get role and assignment details
        role = getUser_ClassroomByCodeAndID(session["user_id"], session["class_code"]).role
        assignment = getAssignmentByID(session["assignment_id"])

        return render_template("assignments/view_assignment.html", class_code=session["class_code"], role = role, assignment = assignment)

@assignment_mod.route("/editassign", methods=["GET", "POST"])
@login_required
def editassign():
    role = getUser_ClassroomByCodeAndID(session["user_id"], session["class_code"]).role
    if role == STUDENT :
        return render_template("auth/no_access.html", msg="You do not have access to this page !")

    if request.method == "GET" :
        session["assignment_id"] = request.args.get('id')
        # get role and assignment details
        role = getUser_ClassroomByCodeAndID(session["user_id"], session["class_code"]).role
        assignment = getAssignmentByID(session["assignment_id"])
        return render_template("assignments/edit_assignment.html", class_code=session["class_code"], role = role, assignment = assignment)

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

        assignment = getAssignmentByID(session["assignment_id"])
        assignment.class_code = session["class_code"]
        assignment.title = request.form["title"]
        assignment.last_date = request.form["last_date"]
        assignment.max_score = request.form["max_score"],
        assignment.description = request.form["description"]
        assignment.doc_file = doc_file
        assignment.pdf_file = pdf_file
        assignment.ppt_file = ppt_file
        assignment.zip_file = zip_file
        db.session.commit()
        return redirect(url_for("assignment.assign", class_code=session["class_code"]))
