a,b=map(int,input().split())
cnt=[0]*b
ans=0

while a>1:
    remain=a%b
    cnt[remain]+=1
    a=a//b

for i in range(len(cnt)):
    ans+=cnt[i]**2

print(ans)