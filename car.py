from driver import Driver

class Car(Driver):

    passengers      = int
    type_car        = str

    def __init__(self, name, last_name, passport, id, type_car, license, passengers):
        super().__init__(name,last_name, passport, id, license)

        self.type_car = type_car

        self.passengers = passengers
        # Self Passengers
        if passengers <= 3:
            self.passengers = int(passengers)
            
        else:
            print("El número de pasajeros es demasiado alta")

           

        
           