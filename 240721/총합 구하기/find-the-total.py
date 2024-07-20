a,b=map(int,input().split())
sum=0
for i in range(a,b):
    if i%6==0 and i%8!=0:
        sum+=i

print(sum)