# create class called fruits that has the following attributes: Name, color, and price
# implement a constructor method and a method function that prints {name,color and price}
# create 5 instances of that class
class Fruits:
    def __init__(self, Name, Color, Price):
        self.Name = Name
        self.Color = Color
        self.Price = Price

    def describe_fruits(self):
        print(f"My favourite fruit is a {self.Name} and it is {self.Color} in color and it goes for Shs.{self.Price} in many supermarkets")

my_banana = Fruits("Banana", "Yellow", 10)
my_banana.describe_fruits()
my_peach = Fruits("Peach", "Orange", 20)
my_peach.describe_fruits()
my_apple = Fruits("Apple", "Red", 30)
my_apple.describe_fruits()
my_grape = Fruits("Grape", "Purple", 40)
my_grape.describe_fruits()
my_strawberry = Fruits("Strawberry", "Red", 50)
my_strawberry.describe_fruits()