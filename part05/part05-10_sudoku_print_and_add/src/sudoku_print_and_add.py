# Write your solution here

def grid_filled(sudoku:list):
    for row in sudoku:
        if 0 in row:
            return True
    return False 


          


def print_sudoku(sudoku: list):
    for row in range(len(sudoku)):
        for col in range(len(sudoku[row])):
            if sudoku[row][col] == 0:
                print("_", end=" ")  # Print underscore but don't modify grid
            else:
                print(sudoku[row][col], end=" ")
            
            if col == 2 or col == 5:
                print(" ", end="")  # Add extra spacing for visual clarity

        print()
        if row == 2 or row == 5:
            print()  # Blank line after every 3 rows


       
           
                
                
                
           
        
  

def add_number(sudoku:list,row_no:int,column_no:int,number:int):

    sudoku[row_no][column_no]=number
   
   



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

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    
    print_sudoku(sudoku)