def isVowel(ch):
    vowel_word = ["a", "e", "i", "o", "u"]
    if ch in vowel_word:
        return True
    return False

result = isVowel("t")
print(result)

