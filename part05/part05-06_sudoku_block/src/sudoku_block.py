# Write your solution here


def check_freq(col):
    freq={}
        
    for value in set(col):
        occurence=col.count(value)
        freq[value]=occurence
    
  
    for value in freq:
        if value==0:
            continue

        if freq[value]>1:
            return False
    
    return True

def block_correct(sudoku,row_no,col_no):
    
    new_matrix=[]
    for row in range(row_no,row_no+3):
        for col in range(col_no,col_no+3):
           new_matrix.append(sudoku[row][col])

       
    

    return check_freq(new_matrix)
      





if __name__=="__main__":
  sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

#   print(block_correct(sudoku, 0, 0))
  print(block_correct(sudoku, 1, 2))