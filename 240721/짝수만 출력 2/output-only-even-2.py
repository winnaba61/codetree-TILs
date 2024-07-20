a,b=map(int,input().split())
if a%2!=0:
    a+=1
if b%2!=0:
    b+=1

for i in range(b,a-1,-2):
    print(i,end=' ')