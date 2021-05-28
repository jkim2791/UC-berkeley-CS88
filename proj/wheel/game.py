from secret import SecretWord
from board import Board

class Game:
    """Run an entire game.

    Initialization defines the player who pickers secret word and one or more guessers.
    play
       - picker picks the secret word from the dictionary held by all players
       - guessers guess in turn looking at the state of the board until the game is done
       - each guesser continues as long as they guess currect letters
       - returns final board
    winner returns the player who picked the last letter.
    """
    def __init__(self, picker, guessers):
        # BEGIN
        self.picker = picker
        self.guessers = guessers
        # END

    def play(self, verbose=True):
        # BEGIN
        s_word = self.picker.word()
        b = Board(SecretWord(s_word))
        while b.done() == False:
            if verbose == True:
                b.display(b)
            guess = self.guessers[0].guess(b)
            b.guess(b,guess)
            if guess in b.misses():
                self.guessers = self.guessers[1:]+[self.guessers.pop(0)]
        return b
        # END

    def winner(self):
        # BEGIN
        return self.guessers[0].name
        # END