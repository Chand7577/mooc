# Write your solution here
# You can test your function by calling it within the following block
def greatest_number(num1,num2,num3):
    list1=[]

    list1.append(num1)
    list1.append(num2)
    list1.append(num3)
    list1.sort()
    return list1[-1]


if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)