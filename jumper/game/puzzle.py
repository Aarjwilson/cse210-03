import random

class Puzzle:

    def __init__(self):
        """
        Initialize the two lists to contain the blank spaces and the letters for the random word.
        """
        self._word = []
        self._blanks = []
    

    def _choose_word(self):
        """
        Generate a random word from a list and convert it to a list of letters and also make a list of blanks to go with it.
        """
        words = ["SOCCER","FOOTBALL","RUGBY","BASKETBALL"]
        word = random.choice(words)
        self._word[:0] = word

        self._blanks = ["_"] * len(self._word)


    def _display(self):
        """
        Display the remaining blanks and al the guessed letters.
        """
        print("")
        for x in range(len(self._word)):
            print(self._blanks[x], end=" ")
        print("")
            
    def _replace(self,letter):
        """
        Replace all the blanks with the guess letter in the correct spots.
        """
        for x in range(len(self._word)):
            if self._word[x] == letter:
                self._blanks[x] = letter
            else:
                continue

    def _check(self,letter):
        """
        Check to see if the letter is in the word to be guessed.
        """

        if letter in self._word:
            correct = True
        else:
            correct = False

        return correct


