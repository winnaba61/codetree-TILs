n = int(input())

for i in range(n):
    left_stars = '*' * (n - i)
    spaces = ' ' * (2 * i)
    right_stars = '*' * (n - i)
    print(left_stars + spaces + right_stars)