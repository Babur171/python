target = 'tiger'
input1 = input('tiger')

while input1 != target:
    output1 = ''
    for pos, char in enumerate(input1):
        if char in target:
            if target[pos] == input1[pos]:
                output1 += [' + char + ']
            else:
                output1 += '(' + char + ')'
        else:
            output1 += char

    print("Clue: " + output1)
    input1 = input1(' ')

print("Found!")