from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# from . import db

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:123@localhost/contactForm"
db=SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("contact-us.html")

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.integer, primary_key==True)
    firstName=db.Column(db.String(120), unique==True)
    lastName=db.Column(db.Integer)
    email_name_=db.Column(db.DATE)
    
def __init__(self, firstName_, lastName_, email_name_):
    self.firstName_=firstName_
    self.lastName_=lastName_
    self.email_name_=email_name_
    
with app.app_context():
    db.create_all()

@app.route("./thanks.html", methods=["POST"])

def thanks():
    if request.method=='POST':
        firstName_=request.form["firstName_"]
        lastName_=request.form["lastName_"]
        email_name_=request.form["email_name_"]
        print(request.form)
        
        print(firstName_, lastName_, email_name_)
        data=Data(firstName_, lastName_, email_name_)
        db.session.add(data)
        db.session.commit()
        
        return render_template("thanks.html")
    
if __name__=='__main__':
    app.debug=True
    app.run()