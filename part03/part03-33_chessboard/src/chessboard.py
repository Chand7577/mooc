# Write your solution here

def chessboard(num):
    for i in range(num):
        for j in range(num):
            if (i+j)%2==0:
                print(1,end="")
            else:
                print(0,end="")
        print()

# Testing the function
if __name__ == "__main__":
    chessboard(6)

