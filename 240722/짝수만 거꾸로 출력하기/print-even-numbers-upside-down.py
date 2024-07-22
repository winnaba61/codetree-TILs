n = int(input())
ans = []

nums=list(map(int,input().split()))
for num in nums:
    if num%2==0:
        ans.append(num)

while ans:
    print(ans.pop())