# Import module models (i.e. User)
from app.auth_module.models import User, Student, Teacher
from app.classroom_module.models import Classroom, User_Classroom
from app.assignment_module.models import Assignment
from app.submission_module.models import Submission

def getNamebyIDandRole(user_id, role) :
    if( role == 1):
        return Student.query.filter(Student.user_id == user_id).first()
    if( role == 0):
        return Teacher.query.filter(Teacher.user_id == user_id).first()

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


#User_Classroom and Classroom Table
def getJoinedClassroom(user_id, session) :
    return session.query(Classroom).join(User_Classroom, User_Classroom.class_code == Classroom.class_code).filter(User_Classroom.user_id == user_id).filter(User_Classroom.role == 1).all()
    #return session.query(Classroom, User_Classroom).filter(User_Classroom.user_id == user_id).filter(User_Classroom.role == 1).filter(User_Classroom.class_code == Classroom.class_code).all()
    # return User_Classroom.query.filter(User_Classroom.user_id == user_id).filter(User_Classroom.role == 1).all()

def getCreatedClassroom(user_id, session) :
    return session.query(Classroom).join(User_Classroom, User_Classroom.class_code == Classroom.class_code).filter(User_Classroom.user_id == user_id).filter(User_Classroom.role == 0).all()

def getAssignmentByClassCode(class_code) :
    return Assignment.query.filter(Assignment.class_code == class_code).all()

def getAssignmentByID(id):
    return Assignment.query.filter(Assignment.assignment_id == id).first()

def getSubmissionByUserIDandAssignID(user_id, assignment_id):
    return Submission.query.filter(Submission.user_id == user_id).filter(Submission.assignment_id == assignment_id).first()

def getSubmissionsForAssign(assignment_id):
    submissions = Submission.query.filter(Submission.assignment_id == assignment_id).all()
    for submission in submissions :
        user_id = submission.user_id
        role = getUserByUserID(user_id).role
        user_object = getNamebyIDandRole(user_id, role)
        submission.user_name = user_object.name
        submission.uid = user_object.tid if role == 0 else user_object.usn
    return submissions

def getSubmissionsByUserIDandClassCode(user_id, class_code):
    submissions = Submission.query.filter(Submission.user_id == user_id).filter(Submission.class_code == class_code).all()
    assignment = Assignment.query.filter(Assignment.class_code == class_code).all()

    assignment_names = {}
    for a in assignment:
        assignment_names[a.assignment_id] = a.title

    return submissions, assignment_names
