# write your solution here


def print_matrix(matrix):
    for row in matrix:
        for col in row:
            print(col,end=" ")
        
        print()



def matrix_sum():
    return sum(row_sums())
  


def matrix_max():
    matrix=getMatrix()
    max_value=0
    for row in matrix:
        for col in row:
            if col>max_value:
                max_value=col

    return max_value




def row_sums():
    matrix=getMatrix() #fetch the matrix 
    sum_row=[]
 
    for row in matrix:
        sum_=0
        for col in row:
            sum_+=col
        sum_row.append(sum_)
    
    return sum_row

def getMatrix():
    matrix=[]
    with open('matrix.txt') as file:
        
        
        for line in file:

            innermatrix=[]
            for number in line.split(","):
                
                number=number.replace("\n","")  # removed line break
                if "-" in number:
                    number=int(number[1:])*-1
                 
                    
                innermatrix.append(int((number)))
                
            matrix.append(innermatrix)
                
    
    return matrix
   



if __name__=="__main__":
    matrix=getMatrix()
    # print(matrix_sum())
   