from car import Car

class UberZ(Car):
    typeCar     = list
    material    = list

    def __init__(self, license, driver, typeCar, material):
        super.__init__(license,driver)
        self.typeCar = typeCar
        self.material = material