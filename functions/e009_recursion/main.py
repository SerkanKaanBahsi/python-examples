def Fibonacci(limit,first=0,second=1,counter=0):
    print(second)
    counter+=1
    if(counter != limit):
        Fibonacci(limit,second,second+first,counter)
    else:
        return

num1=int(input("Please Enter the imit of Fibonacci Series"))
Fibonacci(limit=num1)
