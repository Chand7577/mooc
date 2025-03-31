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



def column_correct(sudoku:list,column_no:int):
    cols=[]
    range_list=[1,2,3,4,5,6,7,8,9,0]
    for row in sudoku:
        cols.append(row[column_no])

  
    if check_freq(cols):
        for value in row:
            while value not in range_list:
                return False

        return True
    
    return False

    










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

    print(column_correct(sudoku, 0))
# print(column_correct(sudoku, 1))