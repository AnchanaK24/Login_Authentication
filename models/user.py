import uuid
from models import db



class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.String(128),  primary_key=True,default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(128))
    mail_id = db.Column(db.String(128))
    password = db.Column(db.String(128))

    def __init__(
            self,
            name,
            mail_id,
            password,
    ):
        self.name = name
        self.mail_id = mail_id
        self.password = password

    @staticmethod
    def add_user(name,mail_id,password):
        user=User(
            name=name,
            mail_id=mail_id,
            password=password

        )

        db.session.add(user)
        db.session.commit()

    @staticmethod
    def get_all_users():
        users = User.query.all()
        return users

    @staticmethod
    def get_user_by_mail_id(mail_id):
        user = User.query.filter_by(mail_id=mail_id).first()
        return user

class Session(db.Model):

    session_id = db.Column(db.String(128),  primary_key=True,default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(128))
    mail_id = db.Column(db.String(128))
    password = db.Column(db.String(128))
    __tablename__='session'

    @staticmethod
    def create_session(session):
        ses = session
        return ses
