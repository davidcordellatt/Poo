from account import Account

class User(Account):

    email       = str
    password    = str
    
    def __init__(self, name, last_name, passport, id, email, password):
        super().__init__(name, last_name, passport, id)

        self.email = email
        self.password = password