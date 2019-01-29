# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013

from abc import ABCMeta, abstractmethod           # need these definitions


class Sequence(metaclass=ABCMeta):
  """Our own version of collections.Sequence abstract base class."""
  
  def __init__(self, sequence):
    self.sequence = sequence

  @abstractmethod
  def __len__(self):
    """Return the length of the sequence."""

  @abstractmethod
  def __getitem__(self, j):
    """Return the element at index j of the sequence."""

  def __contains__(self, val):
    """Return True if val found in the sequence; False otherwise."""
    for j in range(len(self)):
      if self[j] == val:                          # found match
        return True
    return False

  def index(self, val):
    """Return leftmost index at which val is found (or raise ValueError)."""
    for j in range(len(self)):
      if self[j] == val:                          # leftmost match
        return j
    raise ValueError('value not in sequence')     # never found a match

  def count(self, val):
    """Return the number of elements equal to given value."""
    k = 0
    for j in range(len(self)):
      if self[j] == val:                          # found a match
        k += 1
    return k
    
def __eq__(self, other):
    """Return True if both sequences are precisely the same for every element"""
    if len(self) != len(other):
        raise ValueError('sequences not equal regarding their length')
    else:
        try:
            for j in range(len(self)):
                if self[j] == other[j]:
                    continue
            return True
        except ValueError:
            raise ValueError('sequences are not equal')
    
if __name__ == '__main__':
    seq_1 = ['a', 'b', 'c', 'ewa']
    seq_2 = ['a', 'b', 'c', 'ewa']
    m = Sequence()
    print(seq_1.__eq__('seq_2'))
    
