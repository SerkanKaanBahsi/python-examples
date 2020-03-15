class Animal:
    def __init__(self, color, eats):
        # print("Animal")
        self.color = color
        self.eats = eats

    def colour(self):
        print(self.color)

    def food(self):
        print(self.eats)


class Dog(Animal):
    def __init__(self, color, eats):
        super().__init__(color, eats)
        # print("Dog")

    def colour(self):
        print(self.color)

    def food(self):
        print(self.eats)


class Pet:
    def __init__(self, name, paper_number):
        self.name = name
        self.paper_number = paper_number

    def retName(self):
        print(self.name)

    def retNumber(self):
        print(self.paper_number)


class MyPet(Dog, Pet):
    def __init__(self, name, color, eats, paper_number):
        Dog.__init__(self, color, eats)
        Pet.__init__(self, name, paper_number)

    def colour(self):
        print("hello my color is ", self.color)

    def food(self):
        print("I eat ", self.eats)

    def retName(self):
        print("My name is", self.name)

    def retNumber(self):
        print("Dogs Number is ", self.paper_number)


good_boi = Dog("Blue", "Meat")
good_boi.food()
print(isinstance(good_boi, Animal))
print(issubclass(Dog, Animal))

ast = MyPet("Alex", "Black", "Meat", 12231)
ast.food()

# Method Resolution Order
# Looks at classes like trees left right way
print(MyPet.__mro__)
print(MyPet.mro())
# Diamond of death in python
