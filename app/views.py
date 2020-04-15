
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.forms import RegistrationForm
from app.models import Users
from werkzeug.utils import secure_filename
import os, datetime

db.create_all()

@app.route('/',methods=["GET","POST"])
@app.route("/profile",methods=["GET","POST"])
def profile():
    form = RegistrationForm()
    if request.method == "POST" and form.validate_on_submit():
        photo = form.profPic.data
        name = form.first_name.data + " "+ form.last_name.data
        gender = form.gender.data
        email = form.email.data
        location = form.location.data
        bio = form.biography.data
        
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(
            app.config['UPLOAD_FOLDER'], filename
        ))
        
        created_on = getDate()
        user = Users(name,location,gender,email,bio,created_on,filename)
        
        db.session.add(user)
        db.session.commit()
        
        flash("user was successfully added",'success')
        return redirect(url_for("profiles"))
    return render_template("profile.html",form = form)

@app.route("/profile/<userid>")
def user(userid):
    user = Users.query.get(userid)
    name = user.name
    created_on = user.created_on
    location = user.location
    filename = user.img
    gender = user.gender
    email = user.email
    bio = user.bio
    
    return render_template("user.html",user=user,name=name,gender=gender,email=email,location=location,bio=bio,created=created_on,filename=filename)
    
@app.route("/profiles")
def profiles():
    user = Users.query.all()
    return render_template("profiles.html",user=user)

def format_date_joined(date):
    return  "joined " + date

def getDate():
    now = datetime.datetime.now()
    return now.strftime("%B %d,%Y")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
