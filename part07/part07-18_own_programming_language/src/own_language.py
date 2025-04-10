# Write your solution here


def getLocations(commands:list):
    locations={}

    for index in range(len(commands)):
        location=commands[index].strip(":")
        if location.islower():
            locations[location]=index

    
    return locations



def check_operation(var1,var2,op):

    if op == ">=":
        return var1 >= var2
    elif op == "==":
        return var1 == var2
    elif op == "<=":
        return var1 <= var2
    elif op == ">":
        return var1 > var2
    elif op == "<":
        return var1 < var2
    elif op=="!=":
        return var1!=var2
    else:
        raise ValueError(f"Unsupported operator: {op}")


def run(commands):
    result=[]
    
    locations=getLocations(commands)
    dic={
        "A":0,
        "B":0,
        "C":0,
        "E":0,
        "F":0,
        "G":0,
        "H":0,
        "I":0,
        "J":0,
        "K":0,
        "L":0,
        "M":0,
        "N":0,
        "O":0,
        "P":0,
        "Q":0,
        "R":0,
        "S":0,
        "T":0,
        "U":0,
        "V":0,
        "W":0,
        "X":0,
        "Y":0,
        "Z":0,}

    current_line=0  # keep track of the current command
    
    while True:
        
        if current_line==len(commands):
            break
        command=commands[current_line]
      
       
        if len(command.split())==2:
            part1,var=command.split()
            if part1=="JUMP":
                location=var

   
        elif len(command.split())==3:
            part1,var,value=command.split()

        

        elif len(command.split())==6:
            part1,var1,op,var2,instr,location=command.split()
           
        else:
            part1=command.split()[0]
        
        
        
       
     # code to check instruction
       
        if part1=='PRINT':
            try:
                value=dic[var]
            except:
                value=int(var)

            result.append(value)
        
        elif part1=='MOV': 
            if value not in dic:
                dic[var]=int(value)
            
            else:
                dic[var]=int(dic[value])

        elif part1=="ADD":
            if value not in dic:
                dic[var]+=int(value)

            else:
                dic[var]+=int(dic[value])

        elif part1=="SUB":
            if value not in dic:
                dic[var]-=int(value)

            else:
                dic[var]-=int(dic[value])

        elif part1=="MUL":

            if value not in dic:
                dic[var]*=int(value)
            
            else:
                dic[var]*=int(dic[value])

        elif part1=="JUMP":
            if location in locations:
                current_line=locations[location]

        elif part1=="IF":
            var1=dic[var1]
            try:
                var2=dic[var2]
            except:
                var2=int(var2)
            if check_operation(var1,var2,op):
                
                if instr=="JUMP" and location in locations:
                   
                    current_line=locations[location]

        elif part1=='END':
            break
        
        
        current_line+=1
    return result




if __name__=="__main__":
    #test cases
    program4 = []
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)
