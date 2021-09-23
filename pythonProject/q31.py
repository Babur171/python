def filter_long_words(words, n):
  return filter(lambda x: len(x) > n, words)

print(filter_long_words(['that', ' was', 'not', 'funny', 'at', 'all'], 3))