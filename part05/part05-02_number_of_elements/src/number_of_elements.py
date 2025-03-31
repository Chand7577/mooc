# Write your solution here


def count_matching_elements(matrix,target):
    count=0
    for row in matrix:
        for value in row:
            if value==target:
                count+=1

    return count






if __name__=="__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))