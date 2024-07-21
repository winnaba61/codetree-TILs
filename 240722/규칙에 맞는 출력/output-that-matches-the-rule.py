N=int(input())

for i in range(N):
    for j in range(N-i,N+1):
        print(j,end=' ')
    print()