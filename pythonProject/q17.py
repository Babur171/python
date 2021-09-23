import string

def is_palindrome(str1):
  str2 = str1[::-1]
  if str1 == str2:
    return True
  else:
    return False

print(is_palindrome("Go hang a salami I'm a lasagna hog."))
print(is_palindrome("Was it a rat I saw?"))
print(is_palindrome("step on no pets"))
print(is_palindrome("Sit on a potato pan, Otis!"))
print(is_palindrome("Lisa Bonet ate no basil"))
print(is_palindrome("Satan, oscillate my metallic sonatas"))
print(is_palindrome("I roamed under it as a tired nude Maori"))
print(is_palindrome("Rise to vote sir"))
print(is_palindrome("Dammit, I'm mad!"))
print(is_palindrome("This is not a palindrome"))
