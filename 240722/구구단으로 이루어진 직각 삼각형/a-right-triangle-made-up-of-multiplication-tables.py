n=int(input())

for i in range(1,n+1):
    arr=[]
    cnt=1
    for j in range(i,n+1):
        num=cnt*i
        arr.append(f"{i} * {cnt} = {num}")
        cnt+=1
    print(" / ".join(arr))