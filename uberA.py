from car import Car

class UberA(Car):
    typeCar     = list
    material    = list

    def __init__(self, license, driver, passenger, typeCar, material):
        super.__init__(license, driver, passenger)
        self.typeCar = typeCar
        self.material = material