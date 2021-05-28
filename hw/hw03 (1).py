######################
# Required Questions #
######################

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 10)  # 4 * 3 * 2 * 1 # Only n times!!
    24
    """
    if n == 1:
        return 1
    if k == 0:
        return 1
    elif k == 1:
        return n
    else:
        return n * falling(n-1, k-1)


def nonzero(lst):
    """ Returns the first nonzero element of a list

    >>> nonzero([1, 2, 3])
    1
    >>> nonzero([0, 1, 2])
    1
    >>> nonzero([0, 0, 0, 0, 0, 0, 5, 0, 6])
    5
    """
    for n in range (0,len(lst)):
        if lst[n] > 0:
            return lst[n]


def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    length = 1
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length = length + 1
    print(n)
    return length


def odd_even(x):
    """Classify a number as odd or even.
    
    >>> odd_even(4)
    'even'
    >>> odd_even(3)
    'odd'
    """
    if x%2 == 0:
        return 'even'
    elif x%2 == 1:
        return 'odd'


def classify(s):
    """
    Classify all the elements of a sequence as odd or even
    >>> classify([0, 1, 2, 4])
    ['even', 'odd', 'even', 'even']
    """
    classified_odd_even = []
    for i in s:
        classified = odd_even(i)
        classified_odd_even = classified_odd_even + [classified]
    return classified_odd_even


def decode_helper(pair):
    """
    Optional helper function! Could be useful to turn something like [0, 0] to 'Male 0-9'
    """
    if pair[0] == 0:
        total = "Male "
    else:
        total = "Female "
    if pair[1] == 0:
        return total + "0-9"
    if pair[1] == 1:
        return total + "10-19"
    if pair[1] == 2:
        return total + "20-29"
    if pair[1] == 3:
        return total + "30-39"
    if pair[1] == 4:
        return total + "40-49"
    if pair[1] == 5:
        return total + "50-59"
    if pair[1] == 6:
        return total + "60-69"
    if pair[1] == 7:
        return total + "70-79"
    if pair[1] == 8:
        return total + "80-89"
    if pair[1] == 9:
        return total + "90-99"
    if pair[1] == 10:
        return total + "100+"
    

def decode(list_of_sex_age_pairs):
    """
    >>> decode([[0, 0], [1, 1], [1, 10]])
    ['Male 0-9', 'Female 10-19', 'Female 100+']
    >>> decode([[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]])
    ['Male 0-9', 'Male 10-19', 'Male 20-29', 'Male 30-39', 'Male 40-49', 'Female 50-59', 'Female 60-69', 'Female 70-79', 'Female 80-89', 'Female 90-99', 'Female 100+']
    """ 
    return [decode_helper(list_of_sex_age_pairs) for list_of_sex_age_pairs in list_of_sex_age_pairs]
    
    

