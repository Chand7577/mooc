# Write your solution here


def add_remove():
    initialValue=1
    values=[]
    print(f'The list is now {values}')
    choice=input(f'a(d)d, (r)emove or e(x)it:')
    while choice.lower()!='x':
        if choice=='d':
            values.append(initialValue)
            initialValue+=1
            
        
        elif choice=='r':
            if len(values)==0:
                return 
            values.pop()
            initialValue-=1

        print(f"The list is now {values}")
        choice=input(f'a(d)d, (r)emove or e(x)it:')

    print(f"Bye!")


add_remove()