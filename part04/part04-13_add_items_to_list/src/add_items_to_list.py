# Write your solution here


def add_Items(num):
    items=[]
    for i in range(num):
        item=int(input(f"Item {i+1}"))
        items.append(item)

    print(items)
    



num=int(input("How many items:"))
add_Items(num)






