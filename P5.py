m = int(input("請輸入階層值M:"))
n=1
total=1
while (m>total):
    total = total*n
    n=n+1
print("超過M為%d的最小階層為:%d"%(m,n-1))
    