def lingo():
     word = "tiger"
     word = list(word)
     clue = ""
     guess = input("Enter word!:")
     while True:
         for i in range(len(guess)):
             if guess[i] in word:
                 position_in_word = word[i]
                 position_in_guess = guess[i]
                 if position_in_guess == position_in_word:
                     clue = clue+"["+position_in_guess+"]"
                 else:
                     clue = clue+"("+position_in_word+")"
             else:
                 clue = clue + guess[i]
         break
     return clue
print(lingo())