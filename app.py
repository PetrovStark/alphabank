from controller import Controller
from models.user import User


class App:
    def __init__(self):
        self.Controller = Controller(self)
        self.__user = False
        self.__user_wants_to_exit = False

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        if not isinstance(user, User) and not isinstance(user, bool):
            raise Exception(
                'You cannot set this value to this attribute.')

        self.__user = user

    def run(self):
        print('Welcome to AlphaBank.')
        print('Type "help" to see all available procedures')
        while (not self.__user_wants_to_exit):
            procedure = input('\n$  ')

            if procedure == 'exit':
                self.__user_wants_to_exit = True
                continue

            try:
                self.Controller.execute_procedure(procedure)
            except Exception as e:
                print(e)

    def is_authenticated(self):
        if not bool(self.__user):
            raise Exception(
                'You must have been logged in to make this action. Type "login" command.')

        return True


App().run()
