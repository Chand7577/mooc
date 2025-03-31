# Write your solution here


def check_Leap(year):

    if year%400==0 or (year%4==0 and year%100!=0):
        return True
    
    else:
        return False





current_year=int(input("Year:")) 



if check_Leap(current_year):

    next_year=current_year+4
    while check_Leap(next_year)!=True:
        next_year+=4
    
    print(f'The next leap year after {current_year} is {next_year}')

else:
    next_year=current_year+1
    while check_Leap(next_year)!=True:
        next_year+=1


    print(f'The next leap year after {current_year} is {next_year}')

  


