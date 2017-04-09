from app import db

class Classroom(db.Model):
    __tablename__ = "classroom"
    #id = db.Column(db.Integer )
    class_code = db.Column(db.Integer, primary_key = True)
    creator_id = db.Column(db.Integer)
    class_name = db.Column(db.String(255) )
    subject = db.Column(db.String(255))
    subject_code = db.Column(db.String(255) )
    credits = db.Column(db.Integer)
    semester = db.Column(db.Integer)
    description = db.Column(db.String(255))

    def __init__(self, class_code, creator_id, class_name, subject, subject_code, credits, semester, description):
        self.class_code = class_code
        self.creator_id = creator_id
        self.class_name = class_name
        self.subject = subject
        self.subject_code = subject_code
        self.credits = credits
        self.semester = semester
        self.description = description

class User_Classroom(db.Model):
    __tablename__ = "user_classroom"
    user_id = db.Column(db.Integer,  primary_key = True)
    class_code = db.Column(db.Integer, primary_key = True)
    role = db.Column(db.Integer )

    def __init__(self, user_id, class_code, role):
        self.user_id = user_id
        self.class_code = class_code
        self.role = role
