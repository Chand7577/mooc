# Write your solution here


user_input=input("Please type in a string:")


for vowel in ["a",'e','o']:
    if vowel in user_input:
        print(f"{vowel} found")

    else:
        print(f"{vowel} not found")
