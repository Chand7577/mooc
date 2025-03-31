# Write your solution here

"""1st letter: x
2nd letter: c
3rd letter: p
The letter in the middle is p"""

letterOne=input("1st letter:")
letterTwo=input("2nd letter:")
letterThird=input("3rd letter:")

lisst1=[letterOne,letterTwo,letterThird]
# max_letter=max(lisst1)
# min_letter=min(lisst1)

# middle_letter=""
# for letter in lisst1:
#     if letter !=max_letter or letter!=min_letter:
#         middle_letter=letter

lisst1.sort()
print(f"The letter in the middle is {lisst1[1]}")