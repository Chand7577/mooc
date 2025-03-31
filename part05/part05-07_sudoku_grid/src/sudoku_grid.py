# Write your solution here
def check_freq(row):
    freq={}
        
    for value in set(row):
        occurence=row.count(value)
        freq[value]=occurence
    
  
    for value in freq:
        if value==0:
            continue

        if freq[value]>1:
            return False
    
    return True

# check if row is filled correctly
def row_correct(sudoku:list,row_value:int):
    
    range_list=[1,2,3,4,5,6,7,8,9,0]
    row=sudoku[row_value]
   


    if check_freq(row):
        for value in row:
            if value not in range_list:
                return False

        return True
    
    return False

# check for every column
def column_correct(sudoku:list,column_no:int):
    cols=[]
    range_list=[1,2,3,4,5,6,7,8,9,0]
    for row in sudoku:
        cols.append(row[column_no])

  
    if check_freq(cols):
        for value in cols:
            if value not in range_list:
                return False

        return True
    
    return False

# check for each block 
def block_correct(sudoku,row_no,col_no):
    
    new_matrix=[]
    row_no=(row_no//3)*3
    col_no=(col_no//3)*3
    for row in range(row_no,row_no+3):
        for col in range(col_no,col_no+3):
           new_matrix.append(sudoku[row][col])

       
    return check_freq(new_matrix)

# function to check if the grid is filled correctly
def sudoku_grid_correct(sudoku:list):
    # if block_correct(sudoku) and row_correct(sudoku) and column_correct(sudoku):
    #     return True
    # else:
    #     return False

    for row in range(len(sudoku)):
        if not row_correct(sudoku,row):
            return False
        
        if not column_correct(sudoku,row):
            return False

        for col in range(0,9):
            if not block_correct(sudoku,row,col):
                return False

    return True
if __name__=="__main__":
    # sudoku1 = [
    # [9, 0, 0, 0, 8, 0, 3, 0, 0],
    # [2, 0, 0, 2, 5, 0, 7, 0, 0],
    # [0, 2, 0, 3, 0, 0, 0, 0, 4],
    # [2, 9, 4, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 7, 3, 0, 5, 6, 0],
    # [7, 0, 5, 0, 6, 0, 4, 0, 0],
    # [0, 0, 7, 8, 0, 3, 9, 0, 0],
    # [0, 0, 1, 0, 0, 0, 0, 0, 3],
    # [3, 0, 0, 0, 0, 0, 0, 0, 2]
    # ]
    # print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))