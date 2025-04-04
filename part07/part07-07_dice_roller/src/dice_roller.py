# Write your solution here
from random import sample
def getFaceValue(face_values:list):

    return sample(face_values,1)[0]



def roll(die:str):
    dices={"A":[ 3, 3, 3, 3, 3, 6],"B":[2, 2, 2, 5, 5, 5],"C":[1, 4, 4, 4, 4, 4]}
    
    if die in dices:
        return getFaceValue(dices[die])



def play(die1:str,die2:str,times:int):
    die1_wins = 0
    die2_wins = 0
    ties = 0

    for _ in range(times):
        d1 = roll(die1)
        d2 = roll(die2)

        if d1 > d2:
            die1_wins += 1
        elif d2 > d1:
            die2_wins += 1
        else:
            ties += 1

    return (die1_wins, die2_wins, ties)


if __name__=="__main__":
    # for i in range(20):
    #     print(roll("A"), " ", end="")
    # print()
    # for i in range(20):
    #     print(roll("B"), " ", end="")
    # print()
    # for i in range(20):
    #     print(roll("C"), " ", end="")
    result = play("A", "C", 1000)
    print(result)

    # result = play("B", "B", 1000)
    # print(result)
