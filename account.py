class Account: 
    id          = str
    name        = str
    last_name   = str
    passport    = str
    
    def __init__(self, name, last_name, passport, id):
        self.name = name
        self.last_name = last_name
        self.passport = passport
        self.id = id
         
        