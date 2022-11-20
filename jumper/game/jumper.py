
class Jumper:

    def __init__(self):
        """
        Initiate the visual for the jumper using a list with strings and set jumper status to alive = true
        """
        self._image = ["  ___  "," /___\ "," \   / ","  \ /  ","   O   ","  /|\  ","  / \  ","       ","^^^^^^^"]
        self._alive = True


    def _display(self):
        """
        display the jumper by printing out the list
        """
        print("")
        for x in range(len(self._image)):
            print(self._image[x])
        print("")

    def _remove(self):
        """
        remove the top part of the parachute
        """
        self._image.pop(0)

    def _check(self):
        """
        Check to see if the parachute is stil there. If not, then set jumper status to alive = false
        """
        if self._image[0] == "   O   ":
            self._image[0] = "   X   "
            self._alive = False
        else:
            self._alive = True

        return self._alive

