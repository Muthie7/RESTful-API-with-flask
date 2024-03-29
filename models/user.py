from db import db


class UserModel(db.Model):
    __tablename__ = 'users'  # how we tell sqlalchemy to create a new table

    id = db.Column(db.Integer, primary_key=True)  # tell it what columns we want the table to contain
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password): #remove the option to pass in an ID since alchemy automatically assigns one
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return UserModel.query.filter_by(username=username).first()
        # SELECT * FROM users WHERE username=username passed in

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
