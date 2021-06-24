km=float(input("請輸入路程公里數(km):"))
money=75
if (km<1.5):
    money=money
else:
    k=km-1.5
    a=k//0.25
    b=k%0.25
    if(b!=0):
        a=a+1
    money=money+a*5
print("所需車資為:%d"%money)