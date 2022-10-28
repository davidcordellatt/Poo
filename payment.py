class Payment:

    id = str

    def __init__(self, id):
        self.id = id

class Paypal(Payment):

    email     = str
    
    def __init__(self, id, email):
        super().__init__(id)
        self.email = email

class Card(Payment):

    number_card     = int
    password        = int
    account_type    = str

    def __init__(self, id, number_card, password, account_type) -> None:
        super().__init__(id)
        self.number_card = number_card
        self.password = password
        self.account_type = account_type

class Cash(Payment):

    amount = int

    def __init__(self, id, amount):
        super.__init__(id)
        self.amount = amount
