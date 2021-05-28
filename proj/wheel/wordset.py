from utils import lowercase, key_of_max
import string

#
# WordSet class
#
class WordSet:
    """
    Set of unique words, all in lower case and of positive length.
    """
    def __init__(self, text):
        """
        Form a WordSet from a string of words or collection of words.
        """
        # BEGIN Question 2
        if type(text) == str:
            self.text = text.split()
        else:
            self.text = [w for w in text]
        self.word_set = []
        # END Question 2

    def words(self):
        """
        Return sorted list of words in WordSet.

        >>> WordSet("Hi. Hey you. How, the heck, are you?").words()
        ['are', 'heck', 'hey', 'hi', 'how', 'the', 'you']
        """
        # BEGIN Question 2

        self.low = [item.lower() for item in self.text]
        self.word_set = [item.strip('?').strip('"').strip('!').strip(',').strip('--').strip('-').strip('.') for item in self.low]
        self.word_set = sorted(set(self.word_set))
        self.answer = [item for item in self.word_set if item != '']
        return self.answer
       
        # END Question 2

    def __contains__(self, word):
        # BEGIN Question 2
        if word in self.words():
            return True
        else:
            return False
        # END Question 2


#
# Dictionary class
#
class Dictionary(WordSet):
    """
    Construct a dictionary from all the words in a text file.
    Subclass of WordSet with a file based initializer.

    >>> from wordset import Dictionary
    >>> Dictionary('assets/lincoln.txt').words()[55]
    'government'
    """
    def __init__(self, filename):
        with open(filename) as fp:
            text = fp.read()
            WordSet.__init__(self, text)

#
# WordMunch class
#
class WordMunch(WordSet):
    """
    Perform analytics on a set of unique words.

    Subclass of WordSet that provides analytics on the words.
    """
    def filter(self, ffun):
        """Filter set to include only those that satisfy the filter function predicate."""
        # BEGIN
        return [w for w in self.word_set if ffun(w)]
        # END

    def frequency(self):
        """Return a dictionary of the frequency of each letter in the word set."""
        # BEGIN
        dict = {}
        for w in self.word_set:
            for i in range(len(w)):
                l = w[i]
                if l in dict:
                    dict[l] +=1
                else:
                    dict[l] = 1
        return dict
        # END
