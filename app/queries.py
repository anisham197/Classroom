# Import module models (i.e. User)
from app.auth_module.models import User, Student
from app.classroom_module.models import Classroom, User_Classroom

def getUserByUsername(username) :
    return User.query.filter(User.username == username).first()

def getStudentByUsn(usn) :
    return Student.query.filter(Student.usn == usn ).first()

def getClassroomByCode(code) :
    return Classroom.query.filter(Classroom.class_code == code ).first()

def getUserByUserID(user_id) :
    return User.query.filter(User.id == user_id).first()

def getUser_ClassroomByCodeAndID(user_id, class_code) :
    return User_Classroom.query.filter(User_Classroom.user_id == user_id).filter(User_Classroom.class_code == class_code).first()

def getUser_ClassroomByID(user_id) :
    return User_Classroom.query.filter(User_Classroom.user_id == user_id).first()

def getUserClassroom(user_id, session) :
    return session.query(Classroom).join(User_Classroom, User_Classroom.class_code == Classroom.class_code).filter(User_Classroom.user_id == user_id).filter(User_Classroom.role == 1).all()
    #return session.query(Classroom, User_Classroom).filter(User_Classroom.user_id == user_id).filter(User_Classroom.role == 1).filter(User_Classroom.class_code == Classroom.class_code).all()
    # return User_Classroom.query.filter(User_Classroom.user_id == user_id).filter(User_Classroom.role == 1).all()
