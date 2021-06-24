a=0
b=[]
while a!="":
    a=input("輸入每班人數(Enter結束):")
    b.append(a)
c=max(b)

print("須購買的電腦數:%s"%(c))