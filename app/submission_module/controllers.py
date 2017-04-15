from flask import Flask, flash, redirect, render_template, request, session, url_for, Blueprint
from flask_session import Session
from app.helpers import *
#from tempfile import gettempdir
from app import db
from app.queries import *

# Define the blueprint
submission_mod = Blueprint('submit', __name__, url_prefix='/submissions' , static_folder = '../static', template_folder = '../templates/submissions')

@submission_mod.route("/make_submission", methods=["GET", "POST"])
@login_required
def make_submission():
    return render_template("assignments/inside_class.html", role=0, assignments=None)
