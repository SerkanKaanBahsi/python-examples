
#Basically, a decorator takes in a function, adds some functionality and returns it.

#Here is a decorator example.
#In this example some operations must be done without some numbers    
def cantUseNum(func):
    
    def addNum(num1,num2):
        if num1 == 1 or num2 == 1:
            print("Cant Use Number 1 With Addition")
            return
        return func(num1,num2)
    
    def divNum(num1,num2):
        if num2 == 0:
            print("That is not possible")
        elif num1 == 2 or num2 ==2:
            print("Cant Use Number 2 With Division")
            return
        return func(num1,num2)
    
    def mulNum(num1,num2):
        if num1 == 2 or num2 == 2:
            print("Cant use Number 2 With Multiplication")
            return
        return func(num1,num2)
    
    def subNum(num1,num2):
        if num1 == 1 or num2 == 1:
            print("Cant Use Number 1 With Subtraction")
            return 
        return func(num1,num2)
    
    if func.__name__ == "add":
        return addNum
    elif func.__name__ == "div":
        return divNum
    elif func.__name__ == "mul":
        return mulNum
    elif func.__name__ ==  "sub":
        return subNum

@cantUseNum
def add(num1,num2):
    return num1+num2

@cantUseNum
def div(num1,num2):
    return num1/num2

@cantUseNum
def mul(num1,num2):
    return num1*num2

@cantUseNum    
def sub(num1,num2):
    return num1-num2

#We can also chain decorators
def patternFirst(func):
    def inner(*args, **kwargs):
        print('{' * 12)
        func(*args, **kwargs)
        print('}' * 12)
    return inner

def patternSecond(func):
    def inner(*args, **kwargs):
        print('<' * 12)
        func(*args, **kwargs)
        print('>' * 12)
    return inner

@patternFirst
@patternSecond
def printCool(message):
    print(message)
    

add(1,1)
y =(mul(5,4))
print(y)


printCool("Air Bender")

    