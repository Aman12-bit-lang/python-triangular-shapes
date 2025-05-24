#for lower
n = 5
for i in range(1, n + 1):
    print("* " * i)
n = 5
#for upper
for i in range(n):
    print("  " * i + "* " * (n - i))
n = 5  
#for pyramid
for i in range(1, n + 1):
    spaces = ' ' * (n - i)
    stars = '* ' * i
    print(spaces + stars)

