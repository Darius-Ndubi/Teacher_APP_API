import jwt
import os
import datetime

from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions

"""
    Class to create user token to be used as access token upon login
    It has a method that when creating the token, uses the payload as the
    email, sets time for token creation to the current epoch time. 
    sets the token to be not be valid 5 minutes before creation.
    sets the token expiry time to 2 hours.
"""


class UserAuthToken(TokenAuthentication):

    @staticmethod
    def generate_access_token(user):
        pay_load = {"email": user.get('email'),
                    "iat": datetime.datetime.utcnow(),
                    "nbf": datetime.datetime.utcnow() + datetime.timedelta(
                        minutes=-5),
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(
                        minutes=120)
                    }
        # Create token to be used and encode it with applications' key
        jwt_token = jwt.encode(pay_load, os.getenv("SECRET_KEY"))

        jwt_token = str(jwt_token, 'utf-8')
        
        # Return user token created
        return jwt_token

    #  Method to decode user token from request header
    def authenticate_credentials(self, key):
        # First try to decode the token
        # then fetch the user data that concides with the user email
        # If the token is older that 120 mins or 2hrs the token has expired
        # raise a validation error and for user to get a new token
        # ONLY when the token is valid return the user and the decoded payload
        try:
            payload = jwt.decode(key, os.getenv("SECRET_KEY"))
            user = get_user_model().objects.get(email=payload["email"])

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed(
                'Token has expired please request for another'
            )
        return (user, payload)
