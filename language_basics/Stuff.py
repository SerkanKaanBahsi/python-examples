

l=[str(i) for i in range(10)]

l.insert(0,"(")
l.insert(4,")")
l.insert(5," ")
l.insert(9,"-")

print("".join(l))
