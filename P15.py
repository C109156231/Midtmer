a=list(input("輸入一組四位元數字為:"))
num=[]
for i in range(len(a)):
    b=str((int(a[i])+7)%10)
    num.append(b)
tmp=num[0]
num[0]=num[2]
num[2]=tmp
tmp1=num[1]
num[1]=num[3]
num[3]=tmp1

print("輸出加密後的數字:"+"".join(num))