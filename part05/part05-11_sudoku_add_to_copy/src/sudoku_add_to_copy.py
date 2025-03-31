# Write your solution here


def grid_filled(sudoku:list):
    for row in sudoku:
        if 0 in row:
            return True
    return False 

def print_sudoku(sudoku:list):

    if grid_filled(sudoku):
        for row in range(len(sudoku)):
            for col in range(len(sudoku[row])):
                if sudoku[row][col]==0:
                    print("_",end=" ")

                else:
                    print(sudoku[row][col],end=" ")

                  
                if col == 2 or col == 5:
                    print(" ", end="")    #adding extra space for alignment
                    
            print()  
            if row == 2 or row == 5:
                print() #add space after every three rows
           


    else:
        for row in sudoku:
            for _ in row:
                print("_",end=" ")

            print()




def add_number(copy:list,row_no:int,column_no:int,number:int):
   
    copy[row_no][column_no]=number

def copy_and_add(original:list,row_no:int,column_no:int,number:int):
    copy_grid=[row[:] for row in original]
    print(copy_grid)
    add_number(copy_grid,row_no,column_no,number)
    return copy_grid





if __name__=="__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)