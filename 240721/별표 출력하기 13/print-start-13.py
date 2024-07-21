def print_stars(n):
    print('* ' * n)
    
    for i in range(1, n):
        print('* ' * i)
    for i in range(n-1, 0, -1):
        print('* ' * i)
    
    print('* ' * n)

n = int(input())
print_stars(n)