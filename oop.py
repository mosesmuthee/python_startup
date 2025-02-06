# object-oriented programming
# make sure class is in capital letters(starts with a capital)
class Car:
    # constructor method
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    # a method function
    def describe_car(self):
        print(f"My dream car make: {self.make} "
              f"\nMy dream model: {self.model} "
              f"\nYear of manufacture: {self.year}")
        print(f"Car: {self.year} {self.make} {self.model}")
# create object or instances of a class
my_suzuki = Car("Suzuki", "Swift", 2024)
my_suzuki.describe_car()

my_bmw = Car("BMW", "X6", 2022)
my_bmw.describe_car()

my_rolls_royce = Car("Rolls Royce", "Phantom", 2023)
my_rolls_royce.describe_car()