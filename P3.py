year = int(input("西元年:"))
a = ["rat","ox","tiger","rabbit","dragon","snake","horse","sheep","monkey","rooster","dog","pig"]
d=(year-4)%12
print(a[d])