from collections import defaultdict
def anagram_finder(file_name):
	words = []
	with open(file_name, 'r') as f:
		for line in f:
			words.append(line.rstrip())
	anadict = defaultdict(list)
	for word in words:
		key = ''.join(sorted(word))
		anadict[key].append(word)
	longestana = 0
	for anagram, anawords in anadict.items():
		if len(anawords) > longestana:
			longestana = len(anawords)

	for anagram, anawords in anadict.items():
	    if len(anawords) > longestana-1:
             print(anagram, anawords)
anagram_finder('q43.py')