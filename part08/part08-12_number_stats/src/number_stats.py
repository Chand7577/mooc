# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.total=0

    def add_number(self, number:int):
        self.total+=number
        self.numbers+=1

    def count_numbers(self):
        return self.numbers

    def get_sum(self):
        
        return self.total

    def average(self):
        if self.numbers==0:
            return 0
        return self.total/self.numbers


    

stats = NumberStats()
even_numbers=NumberStats()
odd_numbers=NumberStats()
print(f"Please type in integer numbers:")

while True:
    
    input_value=int(input())
    if input_value==-1:
        break

    
    stats.add_number(input_value)
    if input_value%2==0:
        even_numbers.add_number(input_value)

    else:
        odd_numbers.add_number(input_value)
    
    
    
print(f"Sum of numbers: {stats.get_sum()}")
print(f"Mean of numbers: {stats.average()}")
print(f"Sum of even numbers: {even_numbers.get_sum()}")
print(f"Sum of odd numbers: {odd_numbers.get_sum()}")
