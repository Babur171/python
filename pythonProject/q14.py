listOfWords = ['wordOne', 'wordTwo', 'wordThree', 'wordFour', 'wordFive']

listOfInts = []

for i in listOfWords:
    listOfInts.append(len(i))

print("List of words:" + str(listOfWords))
print("List of wordlength:" + str(listOfInts))