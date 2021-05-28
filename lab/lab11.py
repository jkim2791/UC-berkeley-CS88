#############
# Iterators #
#############

# Q2
class IteratorRestart:
    """
    >>> iterator = IteratorRestart(2, 7)
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

    def __iter__(self):
        self.current = self.start
        return self



# Q3
class Str:
    def __init__(self,str):
        self.str = str
        self.count = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count >= len(self.str):
            raise StopIteration
        return self.str[self.count]



##############
# Generators #
##############

# Q4
def countdown(n):
    """
    >>> from types import GeneratorType
    >>> type(countdown(0)) is GeneratorType # countdown is a generator
    True
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    i = n
    while i >= 0:
        yield i 
        i-=1


class Countdown:
    """
    >>> from types import GeneratorType
    >>> type(Countdown(0)) is GeneratorType # Countdown is an iterator
    False
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    def __init__(self, number):
        self.start=number
    def __iter__(self):
        while self.start>=0:
            yield self.start
            self.start-=1


# Q5
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    i = n
    while i >=1:
        if i ==1:
            yield 1
            return 1
        if i %2==0:
            yield i 
            i =i//2
        else:
            yield i 
            i = 3*i +1

