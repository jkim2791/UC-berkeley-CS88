
"""Lab 6: Review """

## Coding

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    if k == 0:
        return False
    else:
        return has_seven( k //10)




def deep_len(lst):
    """Returns the deep length of the list.

    >>> deep_len([1, 2, 3])     # normal list
    3
    >>> x = [1, [2, 3], 4]      # deep list
    >>> deep_len(x)
    4
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> deep_len(x)
    6
    """
    total = 0
    for i in lst:
        if type(i) != list:
            total = total + 1
        if type(i) == list:
            total = total + deep_len(i)
    return total


def polynomial(degree, coeffs):
    """
    >>> fourth = polynomial(4, [3,6,2,1, 100])
    >>> fourth(3)   # 3*(3**4) + 6*(3**3) + 2*(3**2) + 1*(3**1) + 100
    526
    >>> third = polynomial(3, [2, 0, 0, 0])
    >>> third(4)   # 2*(4**3) + 0*(4**2) + 0*(4**1) + 0
    128
    """
    def help(x):
        total, index = 0, 0
        c = degree
        while c > -1:
            total = total + coeffs[index] * (x**c)
            index += 1
            c -= 1
        return total 
    return help
    


def add_matrices(x, y):
    """
    >>> matrix1 = [[1, 3],
    ...            [2, 0]]
    >>> matrix2 = [[-3, 0],
    ...            [1, 2]]
    >>> add_matrices(matrix1, matrix2)
    [[-2, 3], [3, 2]]
    """
    "*** YOUR CODE HERE ***"
    


def mul_by_num(num):
    """
    Returns a function that takes one argument and returns num
    times that argument.
    >>> x = mul_by_num(5)
    >>> y = mul_by_num(2)
    >>> x(3)
    15
    >>> y(-4)
    -8
    """
    "*** YOUR CODE HERE ***"
    


def skip_add(n):
    """ Takes a number x and returns x + x-2 + x-4 + x-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    """
    "*** YOUR CODE HERE ***"



