# import module sys to get the type of exception
import sys

alist = ["s", 1, 0]

for elements in alist:
    try:
        print("Element is = ", elements)
        num = 1 / int(elements)
    except:
        print("Oops!", sys.exc_info()[0], "occured.")
        print("Next Element")
        print()

print(num)

try:
    # num=1/0
    # num=1/int('a')
    num = 1 / 2
except ZeroDivisionError:
    print("Cant divide numbers with 0")
    pass
except ValueError:
    print("Divide an integer with an integer")
    pass
else:
    print(num)
finally:
    print("I am out of here")
