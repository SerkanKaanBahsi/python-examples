def takeNum(num):
    #This is the outer enclosing function
    
    def printNum():
        #This is the nested function
        print(num+2)
    
    return printNum


example = takeNum(3)
example()

#Closures can avoid the use of global values

def takeSqrt(num):
    def calculate(n):
        return n ** num
    return calculate

sqr2 = takeSqrt(2)

sqr7 = takeSqrt(7)

print(sqr2(5))

print(sqr7(3))


