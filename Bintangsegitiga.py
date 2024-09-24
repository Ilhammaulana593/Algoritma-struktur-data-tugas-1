def print_pattern(n):
    for i in range(n):
        spaces = ' ' * (i * 3)
        stars = '* ' * (n - i)
        print(spaces + stars)
n = 7
print_pattern(n)
