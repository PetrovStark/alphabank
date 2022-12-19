from models.user import User


class Controller(object):
    def __init__(self, instance_App):
        self.App = instance_App

    def execute_procedure(self, procedure):
        procedures = {
            'help': Controller.help,
            'register': self.register,
            'login': self.login,
            'logout': self.logout,
            'deposit': self.deposit,
            'withdraw': self.withdraw,
            'extract': self.extract
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

        print('\nWelcome to Alphabank, {}!'.format(user.name))

        return True

    def login(self):
        if (self.App.user != False):
            raise Exception('You are already logged in.\nTo log into another account, you must log out of this one first by typing the "logout" command.')

        email = input('Your e-mail:  ')
        password = input('Your password:  ')
        try:
            self.App.user = User.login(email, password)
            print('Hi, {}!'.format(self.App.user.name))
        except Exception as e:
            print(e)
        
    def logout(self):
        self.App.is_authenticated()
        print('Bye, {}!'.format(self.App.user.name))
        self.App.user = False

    def deposit(self):
        amount = 0
        try:
            self.App.is_authenticated()
            amount = input('Type the amount in U$ Dollars:  ')
            self.App.user.account.deposit(amount)
        except Exception as e:
            print(e)
            return False

        print('You successfully deposited ${} to your account.'.format(amount))

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

        print('You successfully withdrew ${} from your account.'.format(amount))

        return True
    
    def extract(self):
        self.App.is_authenticated()
        print(self.App.user.account.extract())
    
    @staticmethod
    def help():
        procedures = [func for func in dir(Controller) if callable(getattr(Controller, func)) and not func.startswith("_")]
        procedures.append('exit') # Adding the exit procedure, which not has a method.
        procedures.remove('execute_procedure')
        print(procedures)
