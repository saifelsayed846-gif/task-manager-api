from extentions import db

class Task(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    task=db.Column(db.String(200))
    status=db.Column(db.String(20),default='pending')
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))