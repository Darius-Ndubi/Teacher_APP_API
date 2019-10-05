from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from django.db import models


class UserManager(BaseUserManager):

    """
        Class method to create a new user to the application. It handles user
        registration. It takes in user:
            firstName
            lastName
            username
            email
            password
    """

    def create_user(self, firstName, is_teacher,
                    lastName, username, email, password=None,
                    is_active=True):

        """Create and return a new_user with an email, firstName, lastName username and password."""
        user = self.model(firstName=firstName, is_teacher=is_teacher,
                          lastName=lastName, username=username,
                          email=self.normalize_email(email))
        # hash the password
        user.set_password(password)
        user.save()
        return user


"""
    Class to specify the user fields to be added to the database
"""


class User(AbstractBaseUser):
    firstName = models.CharField("User's first name",
                                 max_length=50,
                                 null=False)
    lastName = models.CharField("User's last name", max_length=50, null=False)
    username = models.CharField("User's username", max_length=50, unique=True)
    email = models.EmailField("User's email", max_length=254, unique=True)
    is_teacher = models.BooleanField(default=False)
    password = models.CharField(max_length=254)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()
