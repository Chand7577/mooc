# Write your solution here


current_word=input("Please type in a word:")
prev_word=""
words=[]
while current_word!="end":

    if current_word==prev_word:
        break
    words.append(current_word)
    prev_word=current_word
    current_word=input("Please type in a word:")



for word in words:
    print(word,end=" ")




