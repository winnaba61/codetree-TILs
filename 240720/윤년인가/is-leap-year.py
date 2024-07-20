y=int(input())
ans="true"

if y%4==0:
    if y%100==0 and y%400!=0:
        ans="false"
else:
    ans="false"
    
print(ans)