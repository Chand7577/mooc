
# Write your solution here

def check_list_part(numbers:list):
    converted=0
    
    try:
       for value in range(len(numbers)):
           numbers[value]=int(numbers[value])
           converted=1
    except ValueError:
      converted=0
      return converted
    
    return converted
   


def convert_lottery_values_into_int(numbers:list):
    for value in range(len(numbers)):
        numbers[value]=int(numbers[value])
    
    return numbers


def check_range(numbers:list):
    converted_list=convert_lottery_values_into_int(numbers)
    for value in converted_list:
        if value<1 or value>39:
            return False
    
    return True


def check_length(numbers:list):
    return len(numbers)==7       
  
    

def check_week_part(string:list):
    
    try:
        new_value=int(string[1])
        return True
    except ValueError:
        return False
        

def duplicates(numbers:list):
    dic={}
  
    for value in range(len(numbers)):
        key=numbers[value]
        dic[key]=dic.get(key,0)+1

   
    for key,value in dic.items():
        if value>1:
            return False

    return True  

def filter_incorrect():
    count=1
    with open('lottery_numbers.csv') as file:
        for line in file:
            lottery_list=line.strip().split(";")
            # print(lottery_list)
            week_part=lottery_list[0].split()
            lottery_numbers_list=lottery_list[1].split(',')
            
            if not check_week_part(week_part): # check if the week part contains appropriate value
                continue
            
            
            if not check_list_part(lottery_numbers_list): # check if values in lotter list can be converted into integers
                continue
            
            if not check_length(lottery_numbers_list):   # check length of the lottery lst
                continue  

            if not check_range(lottery_numbers_list): # check if values in in the list are not in the specified range 1-39 inclusive
                continue      

            if not duplicates(lottery_numbers_list): # check if there are duplicates in list                              
                continue
            
            mode='w' if count==1 else 'a'
            count+=1
            with open('correct_numbers.csv',mode) as file:
                file.write(f"{line}") 
           
           
            
            
if __name__=="__main__":
    filter_incorrect()
