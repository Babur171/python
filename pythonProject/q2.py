def maximum(a, b, c):
    if (a > b) and (a > c):
        largest = a

    elif (a < b) and (b > c):
        largest = b
    else:
        largest = c

    return largest


a = 10
b = 14
c = 12
print(maximum(a, b, c))