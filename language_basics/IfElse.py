#If Else Code

a=5
c=int(input("Enter a Number: "))
b=int(input("Enter a Number: "))

if b<=a:
    if b<=c:
        print("%d is the smallest" %b)
    else:
        print("%d is the smallest" %c)
elif a > c:
    print("C is the smallest")
else:
    print("A is the smallest")
