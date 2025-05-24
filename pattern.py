# for lower triangular
for i in range(1, 5 + 1):
    print("* " * i)

#for upper triangular
for i in range(5, 0, -1):
    print("* " * i)

#for pyramid
for i in range(1, 5 + 1):
    print(" " * (5 - i) + "* " * i)


input()
