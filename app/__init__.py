# Import flask and template operators
from flask import Flask, render_template, url_for, redirect

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# # Sample HTTP error handling
# @app.errorhandler(404)
# def not_found(error):
#     return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.auth_module.controllers import auth_mod as auth_module
from app.classroom_module.controllers import classroom_mod as classroom_module
from app.assignment_module.controllers import assignment_mod as assignment_module

# Register blueprint(s)
app.register_blueprint(auth_module)
app.register_blueprint(classroom_module)
app.register_blueprint(assignment_module)
# app.register_blueprint(xyz_module)
# ..

@app.route("/", methods=["GET", "POST"])
def index():
	return redirect(url_for('classroom.index'))

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
