a,b=map(int,input().split())

for i in range(2,9,+2):
    arr=[]
    for j in range(b,a-1,-1):
        num=j*i
        arr.append(f"{j} * {i} = {num}")
    print(" / ".join(arr))
print()