n = int(input())
arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]

cnt = 0  

for i in range(n):
    for j in range(n):
        print(arr[cnt % len(arr)] % 9, end='')
        cnt += 1
    print()