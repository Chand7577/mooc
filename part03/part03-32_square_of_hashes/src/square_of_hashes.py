# Write your solution here
# You can test your function by calling it within the following block

def hash_square(num):
    for row in range(num):
        for col in range(num):
            print("#",end="")

        print()
if __name__ == "__main__":
    hash_square(5)