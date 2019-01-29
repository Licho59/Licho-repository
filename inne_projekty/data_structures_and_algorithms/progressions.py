# Developed for use with the book:
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013

class Progression:
    """Iterator producing a generic progression.
    Default iterator produces the whole numbers 0, 1, 2, ...
    """

    def __init__(self, start=0):
        """Initialize current to the first value of the progression."""
        self._current = start

    def _advance(self):
        """Update self._current to a new value.
        This should be overridden by a subclass to customize progression.
        By convention, if current is set to None, this designates the
        end of a finite progression.
        """
        self._current += 1

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        if self._current is None:    # our convention to end a progression
            raise StopIteration()
        else:
            answer = self._current     # record current value to return
            self._advance()            # advance to prepare for next time
            return answer              # return the answer

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self

    def print_progression(self, n):
        """Print next n values of the progression."""
        print(' '.join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression):  # inherit from Progression
    """Iterator producing an arithmetic progression."""

    def __init__(self, increment=1, start=0):
        """Create a new arithmetic progression.
        increment  the fixed constant to add to each term (default 1)
        start      the first term of the progression (default 0)
        """
        super().__init__(start)                # initialize base class
        self._increment = increment

    def _advance(self):                      # override inherited version
        """Update current value by adding the fixed increment."""
        self._current += self._increment


class GeometricProgression(Progression):   # inherit from Progressio
    """Iterator producing a geometric progression."""

    def __init__(self, base=2, start=1):
        """Create a new geometric progression.
        base       the fixed constant multiplied to each term (default 2)
        start      the first term of the progression (default 1)
        """
        super().__init__(start)
        self._base = base

    def _advance(self):                      # override inherited version
        """Update current value by multiplying it by the base value."""
        self._current *= self._base


class FibonacciProgression(Progression):
    """Iterator producing a generalized Fibonacci progression."""

    def __init__(self, first=0, second=1):
        """Create a new fibonacci progression.
        first      the first term of the progression (default 0)
        second     the second term of the progression (default 1)
        """
        super().__init__(first)              # start progression at first
        self._prev = second - first          # fictitious value preceding the first

    def _advance(self):
        """Update current value by taking sum of previous two."""
        self._prev, self._current = self._current, self._prev + self._current
    
class AbsoluteDifferenceProgression(Progression):
    """Class that extends the Progression class so that each value
    in the progression is the absolute value of the difference between the previous two values."""
    
    def __init__(self, first =2, second=200):
        """The constructor that accepts a pair of numbers as the first two values, using 2 and 200 as the defaults"""
        super().__init__(first)
        self._second = second
        
    def _advance(self):
        "Update current value by taking absolute value of difference between the previous two values"
        self._current, self._second = self._second, abs(self._second - self._current)
        
        
class SquareRootProgresssion(Progression):
    """Each value in the progression is the square root of the previous value."""
    
    def __init__(self, start=65536):
        """The constructor should accept an optional parameter specifying the start value, using 65,536 as a default."""
        super().__init__(float(start))
        self._prev = start
      
    def _advance(self):
        self._current =  round(self._prev ** 0.5, 2)
        self._prev = self._current
      
        

if __name__ == '__main__':
    print('Default progression:')
    Progression().print_progression(10)

    print('Arithmetic progression with increment 5:')
    ArithmeticProgression(5).print_progression(10)

    print('Arithmetic progression with increment 5 and start 2:')
    ArithmeticProgression(5, 2).print_progression(4)

    print('Geometric progression with default base:')
    GeometricProgression().print_progression(10)

    print('Geometric progression with base 3:')
    GeometricProgression(3).print_progression(10)

    print('Fibonacci progression with default start values:')
    FibonacciProgression().print_progression(10)

    print('Fibonacci progression with start values 4 and 6:')
    FibonacciProgression(4, 6).print_progression(10)
    
    f = FibonacciProgression(2, 2)
    f.print_progression(8)
    
    print('Absolute difference values progression start with 2 and 200:')
    AbsoluteDifferenceProgression().print_progression(20)
    
    print('Square root progression with default start value:')
    SquareRootProgresssion(1234567893).print_progression(10)  
