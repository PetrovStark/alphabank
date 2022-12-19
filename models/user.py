from models.account import Account

class User:
    __users = []

    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__password = password
        self.__account = Account(self, 0)
    
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
    def account(self):
        return self.__account
    
    @classmethod
    def login(self, email, password):
        for user in User.__users:
            if user['email'] != email:
                continue
            elif user['password'] == password:
                return user['instance']
            
        raise Exception("Invalid email or password.")

    def register(self, instance):
        User.__users.append({
            'email': self.__email,
            'password': self.__password,
            'instance': instance
        })