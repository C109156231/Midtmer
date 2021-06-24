k=[]
for i in range(1,11):
    a=int(input("請輸入第%d個數字:"%i))
    k.append(a)
b=sorted(k)
c=sorted(k,reverse=True)
print("最大的3個數字為:"+str(c[0])+" "+str(c[1])+" "+str(c[2]))
print("最大的3個數字為:"+str(b[0])+" "+str(b[1])+" "+str(b[2]))