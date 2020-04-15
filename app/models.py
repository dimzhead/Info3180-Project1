from app import db


class Users(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    created_on = db.Column(db.String(30))
    name = db.Column(db.String(80))
    location = db.Column(db.String(80))
    img = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    email = db.Column(db.String(80))
    bio = db.Column(db.String(300))

    def __init__(self,name,location,gender,email,bio,created_on,img):
        self.created_on = created_on
        self.name = name
        self.location = location
        self.img = img
        self.gender = gender
        self.email = email
        self.bio = bio
    
    def __repr__(self):
        return "<User %r>" % self.name