from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# from . import db

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:123@localhost/budapp"
db=SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("contact-us.html")

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.integer, primary_key==True)
    name=db.Column(db.String(120), unique==True)
    amount=db.Column(db.Integer)
    date=db.Column(db.DATE)
    
def __init__(self, email_, amount_, date_):
    self.name=email_
    self.amount=amount_
    self.date=date_
    
with app.app_context():
    db.create_all()

@app.route("./thanks.html", methods=["POST"])

def thanks():
    if request.method=='POST':
        email=request.form["email_name"]
        name=request.form["name_name"]
        date=request.form["date_name"]
        print(request.form)
        
        print(name,amount,date)
        data=Data(name,amount,date)
        db.session.add(data)
        db.session.commit()
        
        return render_template("thanks.html")
    
if __name__=='__main__':
    app.debug=True
    app.run()