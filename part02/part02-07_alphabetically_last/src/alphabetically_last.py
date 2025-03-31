# Write your solution here
"""Sample output
Please type in the 1st word: car
Please type in the 2nd word: scooter
scooter comes alphabetically last."""

firstWord=input("Please type in teh 1st word:")
secondWord=input("Please type in teh 2nd word:")




# while firstWord==secondWord:
#     current_char+=1
#     char_of_secondWord=secondWord[current_char]
#     char_of_firstWord=firstWord[current_char]



if firstWord>secondWord:
    print(f"{firstWord} comes alphabetically last.")


elif secondWord>firstWord:
    print(f"{secondWord} comes alphabetically last.")

else:
    print("You game the same word twice.")