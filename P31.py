ch=int(input("國文:"))
eng=int(input("英文:"))
ma=int(input("微積分:"))
ex=int(input("體育:"))
py=int(input("程式設計:"))

av=(ch+eng+ma+ex+py)/5
dict1={"國文":ch,"英文":eng,"微積分":ma,"體育":ex,"程式設計":py}
item1=list(dict1.items())
a=[ch,eng,ma,ex,py]
b=max(a)
print("平均分數:%5.2f"%av)
if(b==ch):
    print("最高分科目:"+str(item1[0][0])+str(item1[0][1])+"分")
elif(b==eng):
    print("最高分科目:"+str(item1[1][0])+str(item1[1][1])+"分")
elif(b==ma):
    print("最高分科目:"+str(item1[2][0])+str(item1[2][1])+"分")
elif(b==ex):
    print("最高分科目:"+str(item1[3][0])+str(item1[3][1])+"分")
else:
    print("最高分科目:"+str(item1[4][0])+str(item1[4][1])+"分")
c=min(a)
if(c==ch):
    print("最低分科目:"+str(item1[0][0])+str(item1[0][1])+"分")
elif(c==eng):
    print("最低分科目:"+str(item1[1][0])+str(item1[1][1])+"分")
elif(c==ma):
    print("最低分科目:"+str(item1[2][0])+str(item1[2][1])+"分")
elif(c==ex):
    print("最低分科目:"+str(item1[3][0])+str(item1[3][1])+"分")
else:
    print("最低分科目:"+str(item1[4][0])+str(item1[4][1])+"分")

