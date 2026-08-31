from app import db


class User(db.Model):

    id = db.Column(db.Integer,primary_key=True)

    email = db.Column(db.String(200),nullable=False,unique=True)

    name = db.Column(db.String(200),nullable=False)
    
    password = db.Column(db.String(200),nullable=False)


class Chat(db.Model):

    id = db.Column(db.Integer,primary_key=True)

    user_id = db.Column(db.Integer,db.ForeignKey("user.id"),nullable=False)

    question = db.Column(db.String(1000),nullable=False)

    answer = db.Column(db.String(3000),nullable=False)