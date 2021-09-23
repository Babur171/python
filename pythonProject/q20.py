def translate(list_a):
    dic = {"merry": "god", "christmas": "jul", "and": "och", \
           "happy": "gott", "new": "nytt", "year": "år"}
    return list(map(lambda x: dic[x] if x in dic else False, list_a))

ab = ['merry', 'and', 'new', 'sad']  # 'sad' not in the dictionary
print(translate(ab))