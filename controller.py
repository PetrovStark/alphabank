from models.user import User
from models.account import Account


class Controller(object):
    def __init__(self, instanceApp):
        self.App = instanceApp

    def execute_procedure(self, procedure):
        procedures = {
            'help': Controller.help,
            'register': self.register,
            'login': self.login,
            'logout': self.logout,
            'deposit': self.deposit,
            'withdraw': self.withdraw,
            'transfer': self.transfer,
            'extract': self.extract,
            'history': self.history
        }

        if (procedure not in procedures):
            raise Exception(
                'Procedure not found, please try again. (Type "help" to see all available procedures)')

        procedures[procedure]()

    def register(self):
        name = input('Your name: ')
        email = input('Your email:  ')
        password = input('Your password: ')
        user = User(name, email, password)
        user.register(user)
        user.account.history.add('Was created.')

        print('\nWelcome to Alphabank, {}!'.format(user.name))

        return True

    def login(self):
        if (self.App.user != False):
            raise Exception(
                'You are already logged in.\nTo log into another account, you must log out of this one first by typing the "logout" command.')

        email = input('Your e-mail:  ')
        password = input('Your password:  ')
        self.App.user = User.login(email, password)
        self.App.user.account.history.add('Logged in.')
        print('Hi, {}!'.format(self.App.user.name))

    def logout(self):
        self.App.is_authenticated()
        print('Bye, {}!'.format(self.App.user.name))
        self.App.user.account.history.add('Logged out.')
        self.App.user = False

    def deposit(self):
        self.App.is_authenticated()
        amount = input('Type the amount in U$ Dollars:  ')
        self.App.user.account.deposit(amount)
        feedback = 'You successfully deposited ${} to your account.'.format(
            amount)
        self.App.user.account.history.add(feedback)
        print(feedback)

    def withdraw(self):
        self.App.is_authenticated()
        amount = input('Type the amount in U$ Dollars:  ')
        self.App.user.account.withdraw(amount)
        feedback = 'You successfully withdrew ${} from your account.'.format(
            amount)
        self.App.user.account.history.add(feedback)
        print(feedback)

    def extract(self):
        self.App.is_authenticated()
        self.App.user.account.extract()
        self.App.user.account.history.add('Consulted your account\'s extract.')

    def history(self):
        self.App.is_authenticated()
        self.App.user.account.history.add('Consulted your account\'s history.')
        self.App.user.account.history.show()

    def transfer(self):
        self.App.is_authenticated()
        accountId = int(input('Type the destiny account ID:  '))
        amount = float(input('Type the amount in U$ Dollars:  '))
        
        self.App.user.account.transfer(amount, accountId)

    @staticmethod
    def help():
        procedures = [func for func in dir(Controller) if callable(
            getattr(Controller, func)) and not func.startswith("_")]
        # Adding the exit procedure, which not has a method.
        procedures.append('exit')
        procedures.remove('execute_procedure')
        print(procedures)
