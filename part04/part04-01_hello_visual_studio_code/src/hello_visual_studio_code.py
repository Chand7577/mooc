# Write your solution here

editor=input("Editor:").lower()

while editor!="Visual Studio Code".lower():

    if editor=="notepad" or editor=="word":
        print("awful")

    else:
        print("not good")
    
    editor=input("Editor:").lower()


print("an excellent choice!")