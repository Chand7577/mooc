# Write your solution here

# Write your solution here


def shortest(strings):
    if not strings:
        return None

    return min(strings,key=len)


if __name__=="__main__":
    print(shortest(['abc','ab']))