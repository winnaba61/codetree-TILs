def print_stars(n):
    print('* ' * n)
    
    for i in range(n-1):
        if i % 2 == 0:
            print('*')
        else:
            print('* ' * (n - 1))
    
    print('* ' * n)

n = int(input())
print_stars(n)