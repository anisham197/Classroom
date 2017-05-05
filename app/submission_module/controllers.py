import os
from flask import Flask, flash, redirect, render_template, request, session, url_for, Blueprint, send_from_directory
from flask_session import Session
from werkzeug import secure_filename
from datetime import datetime

from app.helpers import *
from app import db
from app.queries import *
from app import app
from app.submission_module.models import Submission

# Define the blueprint
submission_mod = Blueprint('submission', __name__, url_prefix='/submissions' , static_folder = '../static', template_folder = '../templates/submissions')

# For a given file, return whether it's an allowed type or not
def allowed_file(filename, extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in extensions

def getExtensions(assignment):
    extensions = []
    if ( assignment.pdf_file == 1 ):
        extensions.extend(["pdf"])
    if ( assignment.doc_file == 1 ):
        extensions.extend(["doc", "docx"])
    if ( assignment.zip_file == 1 ):
        extensions.extend(["zip"])
    if (assignment.ppt_file == 1 ):
        extensions.extend(["ppt", "pptx"])
    return extensions

@submission_mod.route("/upload", methods=["GET", "POST"])
@login_required
def upload():
    if request.method == "POST":

        id = request.args.get('id')
        assignment = getAssignmentByID(id)
        username = getUserByUserID(session["user_id"]).username
        extensions = getExtensions(assignment)

        file = request.files['file']
        # Check if the file is one of the allowed types/extensions
        #TODO handle else condition
        if file and allowed_file(file.filename, extensions):
            # Make the filename safe, remove unsupported chars
            filename = secure_filename(username + "_" + file.filename)
            # Move the file form the temporal folder to the upload folder we setup
            abs_filepath = os.path.join(os.path.abspath(app.config['UPLOAD_FOLDER']), str(id), filename)
            #Beware of Race Condition
            directory = os.path.dirname(abs_filepath)
            if not os.path.exists(directory):
                os.makedirs(directory)
            # Save file
            file.save(abs_filepath)

            submission = getSubmissionByUserIDandAssignID(session['user_id'], id)
            grade = '-'
            file_format = filename.rsplit('.', 1)[1]
            rel_filepath = os.path.join(app.config['UPLOAD_FOLDER'], str(id))
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if submission == None:
                new_submission = Submission(timestamp, session["user_id"], assignment.class_code, id, grade, file_format, filename, rel_filepath)
                db.session.add(new_submission)
                db.session.commit()
            else :
                submission.timestamp = timestamp
                submission.file_format = file_format
                submission.filename = filename
                submission.filepath = rel_filepath
                db.session.commit()

            # return redirect(url_for('submission.uploaded_file', filename=filename, assign_id=id))
            return redirect(url_for('assignment.viewassign', id=session["assignment_id"]))

@submission_mod.route('/uploads/<filename>')
def uploaded_file(filename):
    assign_id = request.args.get('assign_id')
    submission = getSubmissionByUserIDandAssignID(session['user_id'], assign_id)
    return send_from_directory(os.path.abspath(submission.filepath), submission.filename)

@submission_mod.route('/view_file/<filename>')
def view_file(filename):
    filepath = request.args.get('filepath')
    return send_from_directory(os.path.abspath(filepath), filename)

@submission_mod.route('/view_submissions', methods=["GET","POST"])
def view_submissions():
    if request.method == "GET" :
        session["assignment_id"] = request.args.get('id')
        submissions_data = getSubmissionsForAssign(session["assignment_id"])
        assigment_name = getAssignmentByID(session["assignment_id"]).title
        return render_template("submissions/view_submission_teacher.html", assignment_title = assigment_name, submissions = submissions_data)


@submission_mod.route('/student_gradebook', methods=["GET","POST"])
def student_gradebook():
    if request.method == "GET" :
        submissions, assignment_names = getSubmissionsByUserIDandClassCode(session["user_id"], session["class_code"])
        return render_template("submissions/student_gradebook/view_grades_student.html", submissions = submissions, assign_names=assignment_names)
