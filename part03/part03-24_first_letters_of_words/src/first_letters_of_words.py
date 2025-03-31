# Write your solution here


sentence=input("Please type in a sentence:")


start_char=0

for char in range(len(sentence)):

    if start_char==char:
        print(sentence[start_char])

    elif sentence[char]==" ":
        start_char=char+1

   
    
