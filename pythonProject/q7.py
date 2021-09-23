def reverse(string):
    result = ''
    for word in string:
        result = word+result
    return result
print(reverse("i am testing"))