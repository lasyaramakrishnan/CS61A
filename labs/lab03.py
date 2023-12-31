def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    """
    return lambda x: lambda y: func(x, y)

def keep_ints(cond, n):
   """Print out all integers 1..i..n where cond(i) is true

    >>> def is_even(x):
    ... #Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """

   i = 1 
   while i<= n:
      if cond(i):
         print (i)
      i += 1 

def make_keeper(n): 
    """Returns a function which takes one parameter cond and prints
    out all integers 1..i..n  where calling cond(i) returns True.
 
    >>> def is_even(x):
    ... #Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """

    def keeper(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
            i += 1

    return keeper

def and_add(f, n):
    """Return a new function. This new function takes an
    argument x and returns f(x) + n.

    >>> def square(x):
    ...     return x * x
    >>> new_square = and_add(square, 3)
    >>> new_square(4) # 4 * 4 + 3
    19
    """
    return lambda x: f(x) + n 
