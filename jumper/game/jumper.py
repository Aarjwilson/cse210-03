
class Jumper:

    def __init__(self):
        self._image = ["  ___  "," /___\ "," \   / ","  \ /  ","   O   ","  /|\  ","  / \  ","       ","^^^^^^^"]
        self._alive = True


    def _display(self):
        print("")
        for x in range(len(self._image)):
            print(self._image[x])
        print("")

    def _remove(self):
        self._image.pop(0)

    def _check(self):
        if self._image[0] == "   O   ":
            self._image[0] = "   X   "
            self._alive = False
        else:
            self._alive = True

        return self._alive

