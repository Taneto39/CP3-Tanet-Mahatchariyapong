class Customer:
    name = ""
    lastName = ""
    age = 0

    def addcart(self):
        print("Add to ", self.name, self.lastName, "'s cart.")


customer1 = Customer()
customer1.name = "Tanet"
customer1.lastName = "Mahatchariyapong"
customer1.age = 24
customer1.addcart()

customer2 = Customer()
customer2.name = "Bob"
customer2.lastName = "Baby"
customer2.age = 12
customer2.addcart()

customer3 = Customer()
customer3.name = "Cat"
customer3.lastName = "Katy"
customer3.age = 18
customer3.addcart()

customer4 = Customer()
customer4.name = "Josh"
customer4.lastName = "Bush"
customer4.age = 69
customer4.addcart()
