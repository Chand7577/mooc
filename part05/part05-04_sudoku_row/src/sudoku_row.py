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
def row_correct(sudoku:list,row_value:int):
    
    range_list=[1,2,3,4,5,6,7,8,9,0]
    row=sudoku[row_value]
   


    if check_freq(row):
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
    print(row_correct(sudoku,0))