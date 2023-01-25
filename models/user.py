from models.account import Account
from validators.user import UserValidator

class User:
    users = []

    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__password = password
        self.__Account = Account(self, 0)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
        return True

    @property
    def email(self):
        return self.__email

    @property
    def password(self):
        return self.__password

    @property
    def account(self):
        return self.__Account

    @classmethod
    def login(self, email, password):
        for user in User.users:
            if user['email'] != email:
                continue
            elif user['password'] == password:
                return user['instance']

        raise Exception(
            "Invalid email or password.\nIf you don\'t have an account, please register yourself by typing the \"register\" command.")

    @UserValidator.validate
    def register(self, instance):
        User.users.append({
            'email': self.__email,
            'password': self.__password,
            'instance': instance
        })
