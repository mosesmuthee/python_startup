from inspect import classify_class_attrs


class Dad:
    def football(self):
        print("Dad likes watching football")

class Mum:
    def cooking(self):
        print("Mum loves cooking")

class Boy(Dad):
    def eating(self):
        print("Boy loves eating")

my_boy = Boy()
my_boy.football()
my_boy.eating()

class Girl(Mum):
    def braiding(self):
        print("Girl loves plaiting her hair and knitting knots")

my_girl = Girl()
my_girl.braiding()
my_girl.cooking()

