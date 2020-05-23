def vatCal(Totalprize, Taxrate):
    return Totalprize*(1+(Taxrate/100))
print(vatCal(int(input("Total prize = ")), int(input("Tax rate = "))))