import re
from django.contrib.auth import authenticate, login

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User
from .backend.jwt_auth_token import UserAuthToken

"""
    Class that handles data from the register view to the db.
    It validates the email and password too.
"""


class UserRegisterSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(required=True)
    lastName = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True, validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message=(
                    'Email already associated with account '
                    'Have you tried logging in.'
                    'If you have forgotten password. Kindly reset'
                )
            )
        ]
    )

    password = serializers.CharField(min_length=8, required=True,
        error_messages={
            'min_length': 'Password should at least be 8 characters',
            'required': 'Please provide a password'
        }
    )

    """
        Class of all fields to be included in a request
    """
    class Meta:
        model = User
        # List of all fields in the request
        fields = ['firstName', 'lastName', 'username', 'email', 'password',
                  'is_teacher']

    # Method to validate user password
    def validate_password(self, data):
        # Pattern to check if password is alphanumeric
        alphanumeric = re.match(
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d.*)(?=.*\W.*)[a-zA-Z0-9\S]{8,15}$", data)

        # If the password is not Alphanumeric raise validation error
        if not alphanumeric:
            raise serializers.ValidationError(
                {"message": "Password not Strong Enough," +
                    "It should be Alphanumeric and Contain special characters"}
            )
        return data

    # Method to save article data to the data base.
    def create(self, valid_data):
        return User.objects.create_user(**valid_data)


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, required=True)
    access_token = serializers.SerializerMethodField()

    class Meta:
        model = User
        # List of all fields in the response
        fields = ['email', 'password', 'access_token']

    def get_access_token(self, data):
        return UserAuthToken.generate_access_token(data)

    def validate(self, data):

        #  Check if user email exists in the db
        exists = User.objects.all().filter(email=data['email']).exists()

        # If email does not exist inform the user that they are not registered
        if exists is False:
            raise serializers.ValidationError(
                {"message": "You are not registered, Kindly register to login"}
            )

        # user django Authenticate method to check that user password[hash]
        # and email match
        user = authenticate(email=data['email'], password=data['password'])
        # If the data is None,
        # Give general message of the error to avoid shading light on which
        # credential is wrong
        if user is None:
            raise serializers.ValidationError(
                {"message": "Kindly check your credentials," +
                 "Either Email or password is wrong"}
            )
        return data
