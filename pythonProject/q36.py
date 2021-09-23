import re
def hapax(filepath):
    file = open(filepath/'pythonProject_files/q36.txt')
    words = re.findall('\w+', file.read().lower())
    freqs = {key: 0 for key in words}
    for word in words:
        freqs[word] += 1
    for word in freqs:
        if freqs[word] == 1:
            print('word')


hapax('pythonProject_files/q36.txt')