class Vehicle:
    licenseCode = ""
    serialCode = ""

    def turn_on_air(self):
        print(f"{self.licenseCode}'s AC On!")


class Car(Vehicle):
    pass


class Pickup(Vehicle):
    pass


class Van(Vehicle):
    pass


class EstateCar(Vehicle):
    pass


car1 = Car()
car1.licenseCode = "Car"
pickup1 = Pickup()
pickup1.licenseCode = "Pickup"
van1 = Van()
van1.licenseCode = "Van"
estate1 = EstateCar()
estate1.licenseCode = "Estate"
car1.turn_on_air()
pickup1.turn_on_air()
van1.turn_on_air()
estate1.turn_on_air()
