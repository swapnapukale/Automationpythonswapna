# class ABC:
#     def greeting(self):
#         print(" good morning")
#
#
#
# obj = ABC()
# obj.greeting()
#
#
# class mycar:
#     def cars(self,name):
#         print(" my car name is", name)
#
#
# mc = mycar()
# mc.cars('Baleno')
import math


#instance and static method:
# instance method: we need to create object to acess the method and we need to
# mention the self paremter as arguments
class myclass:
    def m1(self):# instance method
        print("intance method")
#static method: we need to add the @staticmethod keyword in beging of static to access the
# static method no need of creating any object  we can directly call thogh the classname
# self argument should not be there
# if want use self then we need to pass the arfument valu while calling the method
#     @staticmethod
#  #   def m2():
#     def m2(self):
#         print("static method")
#
# mc = myclass()
# mc.m1()
# #myclass.m2()
# myclass.m2('name')


#static method with paremetrr

# class staticclass:
#     @staticmethod
#     def sclass(self,name):
#         print(" my car name is",self,name)
#
# staticclass.sclass(10,'baleno')

"""classmethod"""

# class classmethod:
#     @classmethod
#     def cclass(cls):
#         print("hello")
#
# classmethod.cclass()




""" Declaring variables inside the class  with different variable name and same name
Local variables:
class variables:
global variables:
"""


"""Declaring variables inside the class  with different variable name"""

# i,j = 10,30 # declaring global variables
#
# class calculator:
#     x,y=4,5 # declaring class variables
#
#
#     def add(self,a,b): # declaring local variables
#         print(a+b) #accessing local variable
#         print(self.x*self.y) #accessing class variable
#         print(i+j)
#
# cl = calculator()
# cl.add(100,200)


"""Declaring variables inside the class  with same variable name"""
# a,b = 10,30 # declaring global variables
#
# class calculator:
#     a,b=4,5 # declaring class variables
#
#
#     def add(self,a,b): # declaring local variables
#         print(a+b) #accessing local variable
#         print(self.a*self.b) #accessing class variable
#         print(globals()['a']+globals()['b']) #accessing global variables
#
# cl = calculator()
# cl.add(100,200)

"""named and nameless object"""

# class myclass:
#     def add(self):
#         print("hello world")
# mc = myclass()
# mc.add() # named object
# myclass.add('self') # nameless object


""" converting local variables into class variables"""

# class myclass:
#     def add(self,a,b):
#         print(a,b)
#         self.a = a ## assigning local varible to class variables
#         self.b = b
#
#     def mul(self):
#         print(self.a*self.b)
#
#     @staticmethod
#     def test():
#
# mc = myclass()
# mc.add(3,4)
# mc.mul()

#Python oops program to create a class with an instance variable.


#Python oops program to create a class with Instance methods.


class xyz:
    def __init__(self, name):
        self.name = name

    def printname(self):
        print("name before update",self.name)

    def updatename(self,newname):
        self.name = newname
        print("after update",self.name)


x= xyz("test")
x.printname()
x.updatename("hello")


print('-'*100)



#Python oops program to create a class with class variables.

class xyz:
    fname ="test"
    lastn='hello'

    def printfname(self):
        print("full name is", self.fname, self.lastn)


a= xyz()
a.printfname()

print('-'*100)
#1. Write a Python program to create a class representing a Circle.
# Include methods to calculate its area and perimeter.
import math
class mycircle:
    def __init__(self,radius):
        self.radius = radius

    def areaofcirlce(self):
        area = math.pi*(self.radius**2)
        print("area", area)

    def perofcircle(self):
        perofcircle = 2 * math.pi * self.radius
        print("pari", perofcircle)


x= mycircle(3)
x. areaofcirlce()
x.perofcircle()

