"""Board class for Wheel of Fortune game."""

class Board:
    """Board for Wheel of Fortune with attributes board and guessed.
    Attributes:
       board - list of correct characters or "_" in the secret word
       guessed - list of characters guessed so far

    >>> from secret import SecretWord
    >>> b = Board(SecretWord("bookkeeper"))
    >>> len(b)
    10
    >>> b.guess('o')
    2
    >>> b
    < _ o o _ _ _ _ _ _ _ : o >
    >>> b.done()
    False
    >>> b.guess('k')
    2
    >>> b
    < _ o o k k _ _ _ _ _ : o,k >
    >>> b.guess('j')
    0
    >>> b
    < _ o o k k _ _ _ _ _ : o,k,j >
    >>> b.word()
    ['_', 'o', 'o', 'k', 'k', '_', '_', '_', '_', '_']
    >>> b.guesses()
    ['o', 'k', 'j']
    """
    def __init__(self, secret):
        """Create an initial board with no guesses and a secret."""
        # BEGIN
        self.secret = secret
        self.guess_list = []
        # END

    def __repr__(self):
        return '< ' + " ".join(self.word()) + " : " + ",".join(self.guesses()) + ' >'

    def __len__(self):
        return self.word_len()

    def word_len(self):
        """Return the length of the secret word."""
        # BEGIN
        return len(self.secret)
        # END

    def word(self):
        """Return the current state of guessing the word as a list of characters.
        Unguessed positions are represented by '_'
        Guessed positions hold the character.
        """
        # BEGIN
        lst=[]
        index=0
        for i in range(len(self.secret.word)):  
            lst+=["_"]
        for x in  self.guess_list:
            for i in self.secret.word:
                if i==x:
                    lst[index]=x
                    index+=1
                elif i!=x:
                    index+=1
            index=0
        return lst
        # END

    def guesses(self):
        """Return a list of the characters guessed so far."""
        # BEGIN
        return self.guess_list
        # END

    def hits(self):
        """Return a list of characters correctly guessed."""
        # BEGIN
        lst=[]
        for y in  self.guess_list:
            if y in self.secret.word:
                lst+=[y]
        return lst
        # END

    def misses(self):
        """Return a list of characters incorrectly guessed."""
        # BEGIN
        lst = []
        for i in  self.guess_list:
            if i not in self.secret.word:
                lst += [i]
        return lst
        # END

    def guess(self, char):
        """Update the board to reflect the guess of char.
        Return the number of indices in the secret word where char occurs.
        If char does not appear in the word, this will be 0.
        """
        # BEGIN
        t = 0
        self.guess_list += [char]
        for i in self.secret.word:
            if i == char:
                t += 1
        return t
        # END

    def done(self):
        """Determine if the game is done."""
        # BEGIN
        finish =''
        for word in self.word():
            finish += word
        if finish != self.secret.word:
            return False
        else:
            return True
        # END

    def display(self):
        print(self.word())
        print("Guessed chars: ", self.guesses())