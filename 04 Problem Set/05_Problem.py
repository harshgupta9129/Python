a = (7,9,8,0,0,9)

ans = 0
i = 0
while (i<len(a)):
    if (a[i]==0):
        ans+=1
    i+=1
    
print(ans)