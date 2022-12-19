from models.account import Account
from models.user import User


class Controller(object):
    def __init__(self, instance_App):
        self.App = instance_App # To access logged_user attribute.

    def execute_procedure(self, procedure):
        procedures = {
            'help': Controller.help,
            'register': self.register,
            'login': self.login,
            'deposit': self.deposit,
            'withdraw': self.withdraw
        }

        if (procedure not in procedures):
            raise Exception('Procedure not found, please try again. (Type "help" to see all available procedures)')
        
        procedures[procedure]()

    def register(self):
        name = input('Your name: ')
        email = input('Your email:  ')
        password = input('Your password: ')
        user = User(name, email, password)
        user.register(user)

        print('\nWelcome to Alphabank, {}'.format(user.name))

        return True

    def login(self):
        email = input('Your e-mail:  ')
        password = input('Your password:  ')
        try:
            self.App.user = User.login(email, password)
            print('Welcome, {}'.format(self.App.user.name))
        except Exception as e:
            print(e)

    def deposit(self):
        amount = 0
        try:
            self.App.is_authenticated()
            amount = input('Type the amount in U$ Dollars:  ')
            self.App.user.account.deposit(amount)
        except Exception as e:
            print(e)
            return False

        print('You successfully deposited U${} to your account.'.format(amount))

        return True

    def withdraw(self):
        amount = 0
        try:
            self.App.is_authenticated()
            amount = input('Type the amount in U$ Dollars:  ')
            self.App.user.account.withdraw(amount)
        except Exception as e:
            print(e)
            return False

        print('You successfully withdrew U${} to your account.'.format(amount))

        return True
    
    @staticmethod
    def help():
        procedures = [func for func in dir(Controller) if callable(getattr(Controller, func)) and not func.startswith("_")]
        procedures.append('exit') # Adding the exit procedure, which not has a method.
        procedures.remove('execute_procedure')
        print(procedures)
