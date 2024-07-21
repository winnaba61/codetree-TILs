n = int(input())
temp = 1

for i in range(1, n + 1):
    if i % 2 != 0:
        for j in range(temp, temp + n):
            print(j, end=' ')
        print()
    else:
        for k in range(j + 2, j + 2 + 2 * n, 2):
            print(k, end=' ')  
        temp = k + 1
        print()