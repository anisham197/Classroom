from app import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255) )
    password = db.Column(db.String(255))
    role = db.Column(db.Integer)

    def __init__(self, username, password, role ):
        self.username = username
        self.password = password
        self.role = role

class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer)
    name = db.Column(db.String(255) )
    usn = db.Column(db.String(255))
    branch = db.Column(db.String(255) )
    email = db.Column(db.String(255))

    def __init__(self, user_id, name, usn, branch, email ):
        self.user_id = user_id
        self.name = name
        self.usn = usn
        self.branch = branch
        self.email = email
