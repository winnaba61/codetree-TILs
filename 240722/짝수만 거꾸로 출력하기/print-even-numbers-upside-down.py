n = int(input())
ans = []

for i in range(n):
    num=list(map(int,input().split()))
    for num in nums:
        if num%2==0:
            ans.append(num)

while ans:
    print(ans.pop())