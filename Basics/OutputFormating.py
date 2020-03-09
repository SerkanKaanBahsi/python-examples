x=5
y=4
c=14.221345322
Name="Serkan"
LastName="Bahsi"

print("The value of x", x)
print("This is my name {0} and this is my last name {1} ".format(Name,LastName))
print("This is my name {1} and this is my last name {0} ".format(Name,LastName))
print("This is my name {name} and this is my last name {last} ".format(name=Name,last=LastName))
print(5.5,4.3,2.1,2,sep="/",end="!")
print("This is %3.3f " %c)

num = int(input("Give me a number"))
print(num)