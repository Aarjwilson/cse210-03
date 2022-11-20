from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.puzzle import Puzzle


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        jumper (Jumper): The game's jumper.
        is_playing (boolean): Whether or not to keep playing.
        puzzle (Puzzle): The game's puzzle.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.jumper = Jumper()
        self.puzzle = Puzzle()
        self.guess = ""
        self._is_playing = True
        self._terminal_service = TerminalService()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self.puzzle._choose_word()
        self.puzzle._display()
        self.jumper._display()

        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        self.guess = self._terminal_service.read_text("Guess a letter [a-z]: ")
        
    def _do_updates(self):
        correct = self.puzzle._check(self.guess.upper())
        if correct:
            self.puzzle._replace(self.guess.upper())
        else:
            self.jumper._remove()

        self._is_playing = self.jumper._check()

        if "_" not in self.puzzle._blanks:
            self._is_playing = False
        
        
    def _do_outputs(self):
        self.puzzle._display()
        self.jumper._display()
