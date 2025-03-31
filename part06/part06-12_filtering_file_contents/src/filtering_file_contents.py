# Write your solution here

def getOperator(problem:str):
    for value in problem:
        if value in ["+","-"]:
            return value
        
    
def getNumbers(problem:str):
    operator=getOperator(problem)
    values= problem.split(operator)
    return [values,operator]
   

def getSol(num1:int,num2:int,op:str):
    if op=="+":
        return (num1+num2)
    
    else:
        return (num1-num2)

 
def check_sol(result:int,user_result:int):
    return result==user_result
def filter_solutions():
    students={}
    with open('correct.csv', 'w') as correctFile, open('incorrect.csv', 'w') as incorrectFile, open('solutions.csv') as file:
        for line in file:
            line=line.strip().split(";")
            name=line[0]
            problem=line[1]
            values,operator=getNumbers(problem)
            num1,num2=values
          
            sol=getSol(int(num1),int(num2),operator)
            user_result=int(line[2])

            if check_sol(sol,user_result):
                
                    correctFile.write(f"{name};{problem};{user_result}\n")
            else:
                with open('incorrect.csv','w') as file:
                    incorrectFile.write(f"{name};{problem};{user_result}\n")


if __name__=="__main__":                         
    
    filter_solutions()