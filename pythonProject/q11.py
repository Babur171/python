def generate_n_chars(n, c):
    result = ''
    for i in range(n):
        result += c
    return result
print(generate_n_chars(3, 'c'))