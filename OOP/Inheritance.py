class Animal:
    def __init__(self,color,eats):
        #print("Animal")
        self.color=color
        self.eats=eats
    def colour(self):
        print(self.color)
    def food(self):
        print(self.eats)

class Dog(Animal):
    def __init__(self,color,eats):
        super().__init__(color,eats)
        #print("Dog")
    def colour(self):
        print(self.color)
    def food(self):
        print(self.eats)
class Pet:
    def __init__(self,name,papernumber):
        self.name=name
        self.papernumber=papernumber
    def retName(self):
        print(self.name)
    def retNumber(self):
        print(self.papernumber)

class myPet(Dog,Pet):
    def __init__(self,name,color,eats,papernumber):
        Dog.__init__(self,color,eats)
        Pet.__init__(self,name,papernumber)
    def colour(self):
        print("hello my color is ", self.color)
    def food(self):
        print("I eat ",self.eats)
    def retName(self):
        print("My name is", self.name)
    def retNumber(self):
        print("Dogs Number is ", self.papernumber)
    
goodboi=Dog("Blue","Meat")
goodboi.food()
print(isinstance(goodboi,Animal))
print(issubclass(Dog,Animal))

ast=myPet("Alex","Black","Meat",12231)
ast.food()
#Method Resolution Order 
#Looks at classes like trees left right way 
print(myPet.__mro__)
print(myPet.mro())
#Diamond of death in python