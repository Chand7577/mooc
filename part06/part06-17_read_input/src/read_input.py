# Write your solution here
# Write your solution here


def read_input(string,num1,num2):


    while True:
        try:
            typed_num=int(input(f"{string}"))
            if num1<typed_num<num2:
                return typed_num
            else:
                print(f"You must type in an integer between {num1} and {num2}")
        except ValueError:
            print(f"You must type in an integer between {num1} and {num2}")
            


if __name__=="__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print(f"You typed in: {number}")
