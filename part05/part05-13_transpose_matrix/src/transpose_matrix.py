# Write your solution here
# Write your solution here





def transpose(matrix:list):
    rows=len(matrix)
    cols=len(matrix[0])
    transposed = [[matrix[row][col] for row in range(rows)] for col in range(cols)]

    # Modify original matrix in place
    for i in range(len(transposed)):
        matrix[i] = transposed[i]



if __name__=="__main__":
    matrix=[
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    transpose(matrix)