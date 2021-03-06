import re
filename = input("Enter Filename: ")
filename = "words.txt"
fin = open(filename, "r")
all_lines = fin.readlines()
char_dict = dict()
for line in all_lines:
    line = line[:-1]
    words = line.split(" ")
    for word in words:
        word = re.sub("[^a-zA-Z]+", "", word)
        for c in word:
            if c in char_dict:
                char_dict[c] = char_dict[c] + 1
            else:
                char_dict[c] = 1

sorted_char_dict = sorted(char_dict, key=char_dict.get, reverse=True)

for c in sorted_char_dict:
    print(c, " ", char_dict[c])