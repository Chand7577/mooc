# Write your solution here


while True:
    (print(f"Sample output1 - add an entry, 2 - read entries, 0 - quit"))
    option=int(input(f"Function:"))
    if option==0:
        break

    elif option==1:
        entry=input('Diary entry:')
        with open('diary.txt','a') as file:
            file.write(f"{entry}\n")

        print('Diary saved')
    elif option==2:
        with open('diary.txt') as file:
            print("Entries:")
            print(file.read())
            





print('Bye now')