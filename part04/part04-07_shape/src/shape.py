# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block

def line(char,i):
    print(char*i)


def triangle(width,char1):
    for i in range(1,width+1):
        line(char1,i)

def rectangle(height,char2,width):
    for i in range(1,height+1):
        for j in range(1,width+1):
                print(char2,end="")

        print()
        

def shape(width,char1,height,char2):
    triangle(width,char1)
    rectangle(height,char2,width)



if __name__ == "__main__":
    shape(5, "x", 2, "o")