# Write your solution here




def remove_smallest(numbers:list):
    new_list=[]

    print(min(numbers))
    for value in numbers:
        if value==min(numbers):
            numbers.remove(value)
        else:
            new_list.append(value)


   





if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)