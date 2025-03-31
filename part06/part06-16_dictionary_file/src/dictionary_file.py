# Write your solution here
import time
dic={}


while True:

    print("Sample output1 - Add word, 2 - Search, 3 - Quit")
    option=int(input('Function:'))
   

    if option==1:
      
        with open('dictionary.txt','a') as file1:
            word_finnish=input("The word in Finnish:")
            word_english=input("The word in English:")
            dic[word_finnish]=word_english
            file1.write(f"{word_finnish} - {word_english}\n")
            print(f"Dictionary entry added")

    elif option==2:
       
        search_term=input("Search term:")
        with open('dictionary.txt') as file2:
            for line in file2:
                if search_term in line.strip():
                    print(line.strip())
                  
                    
                

     
                

    else:
        print('Bye!')
        break

