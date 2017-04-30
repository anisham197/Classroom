import os
from flask import Flask, flash, redirect, render_template, request, session, url_for, Blueprint, send_from_directory
from flask_session import Session
from werkzeug import secure_filename
from app.helpers import *
from app import db
from app.queries import *
from app import app

# Define the blueprint
submission_mod = Blueprint('submission', __name__, url_prefix='/submissions' , static_folder = '../static', template_folder = '../templates/submissions')

# For a given file, return whether it's an allowed type or not
def allowed_file(filename, extensions):
    return '.' in filename and filename.rsplit('.', 1)[1] in extensions

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
        if file and allowed_file(file.filename, extensions):
            # Make the filename safe, remove unsupported chars
            filename = secure_filename(username + "_" + file.filename)
            # Move the file form the temporal folder to the upload folder we setup
            file.save(os.path.join( os.path.abspath(app.config['UPLOAD_FOLDER']), filename))

            #return redirect(url_for('submission.uploaded_file', filename=filename))
            return redirect(url_for('assignment.viewassign'))

@submission_mod.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(os.path.abspath(app.config['UPLOAD_FOLDER']), filename)
