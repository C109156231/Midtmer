a=str(input("sA:"))
b=str(input("sB:"))
c=b.split(" ")
n=c.count(a)
if (n==1):
    print("子字串判斷為:YES")
else:
    print("子字串判斷為:NO")