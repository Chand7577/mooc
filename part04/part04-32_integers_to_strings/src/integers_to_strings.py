# Write your solution here

def formatted(list1):
    values=[]
    for value in list1:
       values.append(f"{value:.2f}")


    return(values)




if __name__=="__main__":
    formatted([1.234,0.333,0.1111,3.446])