# Write your solution here


limit=int(input('limit:'))
sum=0
value=1
last_value=0
while sum<limit:
    
    last_value=value
    sum+=value
    value+=1
    
  


print(f"The consecutive sum: {" + ".join([str(x+1) for x in range(last_value)])} = {sum}")