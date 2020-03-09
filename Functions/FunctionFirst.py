def SayName(name):
    """This Function
    Says The Name Of User"""
    print("Hello", name)

def Calculate(num1,num2):
    """This Function Adds Two Numbers
    and Returns The Result"""
    return num1+num2

def NoOne():
    """This Function Prints The Word
    Empty and Return Nothing"""
    return

name=input("Please Enter Your Name")
SayName(name)
num1=12
num2=13
num3=Calculate(num1,num2)
print(num3)
print(NoOne())

print(SayName.__doc__)
print(Calculate.__doc__)
print(NoOne.__doc__)
