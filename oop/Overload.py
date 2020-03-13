class Space:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    # overloading the "+" operator
    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        return Space(x,y)



new_Space=Space(5,3)
second_Space=Space(7,12)
print(new_Space)
#same with
print(str(new_Space))
print(format(new_Space))
#it actually does new_Space.__str__()

print(new_Space+second_Space)

#You can overload other operators as well even the comparision operators
