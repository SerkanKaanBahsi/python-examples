x=4
y=5
def change():
    global x
    y=2
    x=x*2
    print(x)
    print(y)
print(x)
change()
print(x)