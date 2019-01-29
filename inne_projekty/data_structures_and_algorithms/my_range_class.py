# Developed for use with the book:
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
import timeit

class Range:
    """A class that mimic's the built-in range class."""

    def __init__(self, start, stop=None, step=1):
        """Initialize a Range instance. Semantics is similar to built-in range class.
        """
        if step == 0:
            raise ValueError('step cannot be 0')
        if stop is None:               # special case of range(n)
            start, stop = 0, start     # should be treated as if range(0,n)
        # calculate the effective length once
        self._length = max(0, (stop - start + step - 1) // step)
        # need knowledge of start and step (but not stop) to support __getitem__
        self._start = start
        self._step = step

    def __len__(self):
        """Return number of entries in the range."""
        return self._length

    def __getitem__(self, k):
        """Return entry at index k (using standard interpretation if negative)"""
        if k < 0:
            k += len(self)       # attempt to convert negative index
        if not 0 <= k < self._length:
            raise IndexError('index out of range')

        return self._start + k * self._step
        

class MyRange(Range):
    """The class with optimized function for checking if item in sequence."""
    
    def __init__(self, start, stop=None, step=1):
        super().__init__(start, stop, step)
    
    def __contains__(self, k):
        if self._start <= k < self._length and (k - self._start) % self._step == 0:
            return True
        
if __name__ == '__main__':
    r = MyRange(0, 1000000, 2)
    print(2 in r)
    print(999999 in r)
    
    t1 = timeit.Timer("99999 in Range(1, 100000, 2)",
                      "from __main__ import Range")
    t2 = timeit.Timer("99999 in MyRange(1, 100000, 2)",
                      "from __main__ import MyRange")
    print("original Range Class, time consumes :", t1.timeit(100))
    print("MyRange Class, time consumes :", t2.timeit(100))
