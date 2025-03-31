# Write your solution here
"""
input 5 6 7
1     1 1 1
2     5 6 7
3     2 2 2
4     4 5 6
5     3 3 3
6       4 5 
7         4 
8
9
10


"""
num=int(input("Please type in a numbers:"))
numbers=[value for value in range(1,num+1)]



while numbers:
    print(numbers.pop(0))
    numbers.reverse()
