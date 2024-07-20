cnt=0

for i in range(3):
    a,b=input().split()
    if a=='Y' and int(b)>=37:
        cnt+=1

if cnt>=2:
    print('E')
else:
    print('N')