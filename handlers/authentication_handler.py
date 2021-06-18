import json

from flask import request,Blueprint
from status import Status
from helpers.exceptions import UserNotFoundException
from services.authentication_service import AuthenticationService

AUTHENTICATION = Blueprint(
    'authentication',
    __name__,
    url_prefix='/api/V1'
)

@AUTHENTICATION.route('/signup', methods=['POST'])
def signup():
    payload = request.get_json(force=True)
    AuthenticationService.signup(payload=payload)
    return json.dumps({"message": "account created successfully"}), Status.HTTP_201_CREATED

@AUTHENTICATION.route('/users')
def get_users():
    users=AuthenticationService.get_all_users()
    return json.dumps({"users": users}), Status.HTTP_200_OK


@AUTHENTICATION.route('/sign-in', methods=['POST'])
def sign_in():
    try:
        payload = request.get_json(force=True)
        response = AuthenticationService.sign_in(payload=payload)
        return json.dumps(response), Status.HTTP_200_OK

    except UserNotFoundException as e:
        return json.dumps({"message": e.message})

