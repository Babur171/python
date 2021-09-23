def overlapping(list1, list2):
    return len([elen for elen in list1 if elen in list2]) > 0

a = [3,4,5,6,7]
b = [6,7,8,9,10]
c = [91,92,93]

print(overlapping(a,b))
print(overlapping(a,c))