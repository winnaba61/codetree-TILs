arr = [[0]*4 for _ in range(4)]
ans=0

for i in range(4):
    arr[i]=list(map(int, input().split()))

for i in range(4):
    for j in range(i+1):
        ans+=arr[i][j]

print(ans)