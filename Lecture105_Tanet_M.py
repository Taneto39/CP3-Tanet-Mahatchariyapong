class Vehicle:
    licenseCode = ""
    serialCode = ""

    def turnon_air(self):
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
car1.turnon_air()
pickup1.turnon_air()
van1.turnon_air()
estate1.turnon_air()
