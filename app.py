from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from app import db as db

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:123@localhost/contactform"
db=SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("./contact-us.html")

class Data(db.Model):
    __tablename__="data"
    # id=db.Column(db.integer)
    firstName=db.Column(db.String(120), unique=False)
    lastName=db.Column(db.String(120), unique=False)
    email_name_=db.Column(db.String(120), unique=True)
    subject_=db.Column(db.String(240), unique=True)
    
def __init__(self, firstName_, lastName_, email_name_, subject_):
    self.firstName_=firstName_
    self.lastName_=lastName_
    self.email_name_=email_name_
    self.subject_=subject_
    
with app.app_context():
    db.create_all()

@app.route("./template/thanks", methods=["POST"])

def thanks():
    if request.method=='POST':
        firstName_=request.form["firstName_"]
        lastName_=request.form["lastName_"]
        email_name_=request.form["email_name_"]
        subject_=request.form["subject_"]
        print(request.form)
        
        print(firstName_, lastName_, email_name_, subject_)
        data=Data(firstName_, lastName_, email_name_, subject_)
        db.session.add(data)
        db.session.commit()
        
        return render_template("thanks.html")
    
if __name__=='__main__':
    app.debug=True
    app.run()