""" creating constructor"""


class mycar:
    def name(self):# instance method
        print("hello my car")

    def __init__(self):# constructor
        print(" this is constructor")

mc = mycar()
mc.name()


"""calling a current class method into another method"""

class main:
    def __init__(self):
        print("hello good morning")
        self.m2(100)
    def m2(self,a):
        print(" this is another method", a)

c = main()
