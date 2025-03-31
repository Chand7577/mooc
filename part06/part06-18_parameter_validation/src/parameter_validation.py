# Write your solution here
# Write your solution here

def new_person(name:str,age:int):

    if name=="":
        raise ValueError("name cannot be empty!")
    
    if len(name.split())<2:
        raise ValueError("name cannot be less than two words!")
    
    if len(name)>40:
        raise ValueError('name cannot be longer than 40 characters!')
    
    if age<0:
        raise ValueError("Age cannot be negative")
    if age>150:
        raise ValueError('Age cannot be greater than 150')
    

    return (name,age)
if __name__=="__main__":
    print(new_person('am',121))
