a=(input("輸入五張牌:"))
k=a.split(" ")
for i in range(len(k)):
    if(k[i]=="A"):
        k[i]=1
    elif(k[i]=="J"):
        k[i]=11
    elif(k[i]=="Q"):
        k[i]=12
    elif(k[i]=="K"):
        k[i]=13
    else:
        k[i]=k[i]
print(k)
b=int(k[0])+int(k[1])+int(k[2])+int(k[3])+int(k[4])
print(b)