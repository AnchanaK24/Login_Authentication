from helpers.exceptions import UserNotFoundException

from models.user import User


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

        if user.password != password:
            raise UserNotFoundException(message="User Not Found ..!!!!")

        response = {
            "user_id": user.id
        }

        return response

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
    def get_user_by_mail_id(mail_id):
        user = User.query.filter_by(mail_id=mail_id).first()
        return user
