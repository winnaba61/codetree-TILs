n=int(input())

c=65
for i in range(1,n+1):
    for j in range(1,i):
        print(' ',end=' ')
    for k in range(n-i+1):
        print(chr(c%65+65),end=' ')
        c+=1
    print()