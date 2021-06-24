ans = list(input("please input your number:"))
a = list("2594")
b=0
c=0


for i in range(len(a)):
    for j in range(len(ans)):
        if a[i]==ans[j] and a[i]==ans[i]:
            b=b+1
        if a[i]==ans[j] and a[i]!=ans[i]:
            c=c+1
print(str(b)+"A"+str(c)+"B")