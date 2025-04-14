# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):

        if len(player1_word)>len(player2_word):
            return 1

        elif len(player1_word)<len(player2_word):
            return 2

        else:
            return 0



class MostVowels(WordGame):
        def __init__(self,rounds):
            super().__init__(rounds)


        def round_winner(self,word1:str,word2:str):
            vowels=["a","e","i","o","u"]
            word1=[vowel for vowel in word1 if vowel in vowels]
            word2=[vowel for vowel in word2 if vowel in vowels]
          

            if len(word1)>len(word2):
                return 1

            elif len(word1)<len(word2):
                return 2

            else:
                return 0


class RockPaperScissors(WordGame):
    def __init__(self,rounds):
            super().__init__(rounds)

    def round_winner(self,word1:str,word2:str):
        valid_options=["scissors","rock","paper"]
        if word2 not in valid_options and word1 not in valid_options:
            pass

        elif word1 not in valid_options:
            return 2

        elif word2 not in valid_options:
            return 1

        elif word1==valid_options[0] and word2==valid_options[2]:
            return 1

        elif word1==valid_options[1] and word2==valid_options[0]:
            return 1

        elif word1==valid_options[2] and word2==valid_options[0]:
            return 2

        elif word1==valid_options[0] and word2==valid_options[1]:
            return 2
        

        elif word1==valid_options[1] and word2==valid_options[2]:
            return 2

        elif word1==valid_options[2] and word2==valid_options[1]:
            return 1

        else:
            pass

       
if __name__=="__main__":
    rps=RockPaperScissors(4)
    rps.play()
