from account import Account

class Driver(Account):
    
    license         = str

    def __init__(self, name, last_name, passport, id, license):
        super().__init__(name, last_name, passport, id)

        self.license = license
        # Self License
        if len(license) == 7:
            self.license = license
        
        elif len(license) > 7:
            print("Hay digitos de más.")
        else:
            print("Faltan digitos en tu placa.")
        
 
        
        