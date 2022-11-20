import random

class Puzzle:

    def __init__(self):
        self._word = []
        self._blanks = []
    

    def _choose_word(self):
        words = ["SOCCER","FOOTBALL","RUGBY","BASKETBALL"]
        word = random.choice(words)
        self._word[:0] = word

        self._blanks = ["_"] * len(self._word)


    def _display(self):
        print("")
        for x in range(len(self._word)):
            print(self._blanks[x], end=" ")
        print("")
            
    def _replace(self,letter):
        for x in range(len(self._word)):
            if self._word[x] == letter:
                self._blanks[x] = letter
            else:
                continue

    def _check(self,letter):

        if letter in self._word:
            correct = True
        else:
            correct = False

        return correct


