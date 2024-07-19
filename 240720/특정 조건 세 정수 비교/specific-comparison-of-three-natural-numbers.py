a,b,c=map(int,input().split())
min_num=min(a,b,c)
if a==min(a,b,c):
    ans_1=1
else:
    ans_1=0

if a==b==c:
    ans_2=1
else:
    ans_2=0

print(ans_1,ans_2)