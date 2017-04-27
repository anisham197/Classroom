from app import db

class Assignment(db.Model):
    __tablename__ = "assignment"
    assignment_id = db.Column(db.Integer, primary_key = True)
    class_code = db.Column(db.Integer)
    title = db.Column(db.String(255))
    last_date = db.Column(db.Date)
    max_score = db.Column(db.Integer)
    description = db.Column(db.Text(65535))
    doc_file = db.Column(db.Boolean)
    pdf_file = db.Column(db.Boolean)
    ppt_file = db.Column(db.Boolean)
    zip_file = db.Column(db.Boolean)


    def __init__(self, class_code, title, last_date, max_score, description, doc_file, pdf_file, ppt_file, zip_file):
        self.class_code = class_code
        self.title = title
        self.last_date = last_date
        self.max_score = max_score
        self.description = description
        self.doc_file = doc_file
        self.pdf_file = pdf_file
        self.ppt_file = ppt_file
        self.zip_file = zip_file
