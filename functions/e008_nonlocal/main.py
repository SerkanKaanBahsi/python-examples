def first():
    x=2
    def second():
        nonlocal x
        x=x+2
        print("inner", x)
    second()
    print("outer", x)
first()