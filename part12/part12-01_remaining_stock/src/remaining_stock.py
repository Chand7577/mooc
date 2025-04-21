# Write your solution here:

def sort_by_remain(product:tuple):
    return product[2]

def sort_by_remaining_stock(products:list):
    new_list=sorted(products,key=sort_by_remain)
    return new_list


if __name__=="__main__":
    products = [("banana", 5.95, 12), ("apple", 3.95, 3), ("orange", 4.50, 2), ("watermelon", 4.95, 22)]


    for product in sort_by_remaining_stock(products):
    
        print(f"{product[0]} {product[2]} pcs")
    
