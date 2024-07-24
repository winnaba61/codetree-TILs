n=int(input())
arr = list(map(int, input().split()))
ans=[]

for i in range(n-1):
    ans.append(arr[i+1]-arr[i])

print(min(ans))