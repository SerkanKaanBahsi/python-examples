#Python is a multi-paradigm programming language.
#Meaning it supports different programing approach

#An object has two characteristics: Attributes, Behavior
#Inheritance: A process of using details from a new class without modifying existing class.
#Encapsulation: Hiding the private details of a class from other objects.
#Polymorphism: A concept of using common operation in different ways for different data input.
#An object (instance) is an instantiation of a class. instantiation = örnekleme
#When class is defined, only the description for the object is defined. Therefore, no memory or storage is allocated.

class Human:
    """This is a class for humans"""
    #Class attribute
    species = "Mammal"
    #instance attribute
    def __init__(self,name,age):
        self.name= name
        self.age= age
        #Encapsulation
        self.__weight=90
    def does(self,action):
        return "{} does {}".format(self.name,action)
    def setWeight(self,newweight):
        self.__weight=newweight
print(Human.__doc__)
#instantiate the Human class
ser=Human("Serkan",21)
dog=Human("Doğa",21)
print("Serkan is a {}".format(ser.__class__.species))
print("{} is {} years old".format(ser.name,ser.age))
print(ser.does("Homework"))
#Adding new attributes
ser.favoritecolor="Blue"
print(ser.favoritecolor)
#print(dog.favoritecolor)
del Human.does
#ser.does("homework")

