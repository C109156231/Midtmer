eng=str(input("請輸入英文句子:"))
a=eng.split(" ")
tmp=[]
for i in range (len(a)-1,-1,-1):
    tmp.append(a[i])
print(tmp)
