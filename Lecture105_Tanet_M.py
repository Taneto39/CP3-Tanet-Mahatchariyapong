class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAC(self):
        print("AC On!")

class Car(Vehicle):
    pass
class Pickup(Vehicle):
    pass
class Van(Vehicle):
    pass
class EstateCar(Vehicle):
    pass

car1 = Car()
pickup1 = Pickup()
van1 = Van()
estate1 = EstateCar()
car1.turnOnAC()
pickup1.turnOnAC()
van1.turnOnAC()
estate1.turnOnAC()
