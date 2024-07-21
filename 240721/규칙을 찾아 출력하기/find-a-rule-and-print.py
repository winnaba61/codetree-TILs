n=int(input())

for i in range(n):
    for j in range(n):
        if n<=1:
            print('*', end=' ')
        else:
            if (i and j)!=0 and (i and j)!=n-1 and i<=j:
                print(' ', end=' ')
            else:
                print('*', end=' ')
    print()