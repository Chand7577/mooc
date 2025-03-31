# Write your solution here
# You can test your function by calling it within the following block

def line(num,char):
    
    if char=="":
        print(num*"*")
    else:
        char=char[0]
        print(num*char)
if __name__ == "__main__":
    line(5, "XXX")