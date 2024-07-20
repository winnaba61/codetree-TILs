cnt=0
for i in range(5):
    num=int(input())
    if num%3==0:
        cnt+=1
    else:
        break

if cnt==5:
    print(1)
else:
    print(0)