import jwt
from helpers.exceptions import UserNotFoundException
from flask import session
from models import User,Session
import uuid,datetime


def token_id(args):
    pass


class AuthenticationService:

    @classmethod
    def signup(cls, payload):
        name = payload.get('name')
        mail_id = payload.get('mail_id')
        password = payload.get('password')

        User.add_user(
            name=name,
            mail_id=mail_id,
            password=password
        )

    @classmethod
    def sign_in(cls, payload):
        mail_id = payload.get('mail_id')
        password = payload.get('password')
        user = User.get_user_by_mail_id(mail_id=mail_id)

        if user.password == password:
            session[mail_id]=[mail_id]
            session_id = str(uuid.uuid4())
            ses = Session(
                session_id=session_id,
                mail_id=payload.get('mail_id'),
                name=payload.get('name'),
                token_id=token_id
            )
            Session.create_session(ses)
            response=session_id
            return response
        else:
            raise UserNotFoundException(message="User Not Found ..!!!!")

    @staticmethod
    def get_all_users():
        users = User.get_all_users()
        data = []
        for user in users:

            user_dict = dict(
                id=user.id,
                name=user.name,
                mail_id=user.mail_id,
                password=user.password
            )
            data.append(user_dict)
        return data
    
     @staticmethod
    def verify_user():
        auth = request.authorization
        if auth and auth.password == 'password':
            token = jwt.encode( {'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)})
            response=({'token': token.encode('UTF-8')})
            return response
        else:
            return({"Message":"User Not Found"})

