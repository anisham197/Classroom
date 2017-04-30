from app import db

class Submission(db.Model):
    __tablename__ = "submission"
    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.String(50))
    user_id = db.Column(db.Integer)
    class_code = db.Column(db.Integer)
    assignment_id = db.Column(db.Integer)
    grade = db.Column(db.String(50))
    file_format = db.Column(db.String(50))
    filename = db.Column(db.String(255))
    filepath = db.Column(db.String(1000))


    def __init__(self, timestamp, user_id, class_code, assignment_id, grade, file_format, filename, filepath):
        self.timestamp = timestamp
        self.user_id = user_id
        self.class_code = class_code
        self.assignment_id = assignment_id
        self.grade = grade
        self.file_format = file_format
        self.filename = filename
        self.filepath = filepath
