x=int(input("X軸座標:"))
y=int(input("Y軸座標:"))
if(x>0 and y>0):
    a="第一象限"
elif(x>0 and y<0):
    a="第四象限"
elif(x<0 and y<0):
    a="第三象限"
elif(x<0 and y>0):
    a="第二象限"
elif(x==0 and y>0):
    a="上半平面Y軸上"
elif(x<0 and y==0):
    a="左半平面X軸上"
elif(x>0 and y==0):
    a="右半平面X軸上"
elif(x==0 and y<0):
    a="下半平面Y軸上"
else:
    a="原點"

b=x*x+y*y
print("該點位於%s，離圓點距離為%d"%(a,b))