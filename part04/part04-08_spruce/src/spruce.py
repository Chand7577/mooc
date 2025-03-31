# Write your solution here
# You can test your function by calling it within the following block



def spruce(num):
    print("a spruce!")
    spaces=num-1
    stars=1
    for _ in range(num):
        print(" "*spaces,end="")
        print("*"*stars)
        spaces-=1
        stars+=2

    # star at last in the middle of the triangle
    spaces=num-1
  
    for i in range(spaces):
        print(" ",end="")
    
    print("*")






if __name__ == "__main__":
    spruce(5)