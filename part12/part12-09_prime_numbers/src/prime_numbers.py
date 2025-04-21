# Write your solution here

def prime_numbers():
    starting=2
    while True:
        divisible=False
        for value in range(2,starting-1):
            if starting%value==0:
                divisible=True
                break

        if not divisible:
            yield starting

        starting+=1


if __name__=="__main__":
    numbers=prime_numbers()
    for i in range(8):
        print(next(numbers))
        
