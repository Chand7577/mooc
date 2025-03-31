# Write your solution here





values=[]
value=int(input("New Item:"))

while value!=0:

    values.append(value)
    print(f'The list now: {values}')
    print(f'The list in order: {sorted(values)}')
    value=int(input("New Item:"))



print(f"Bye!")