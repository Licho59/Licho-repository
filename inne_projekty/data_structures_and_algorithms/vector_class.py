# Developed for use with the book:
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013

import collections


class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        else:
            self._coords = []
            for j in range(len(d)):
                if isinstance(d[j], (int, float)):
                    self._coords.append(d[j])
                else:
                    raise TypeError('invalid parameter type')

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):          # relies on __len__ method
            raise ValueError('dimensions must agree')
                
        result = Vector(len(self))           # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
            
    def __radd__(self, other): # Necessary to use if first arg might not be a vector!!
        """Return sum of two vectors."""
        if len(self) != len(other):   # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))           # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
        
    def __mul__(self, b):
        if isinstance(b, (int, float)):
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = self[i] * b
            return result
        elif isinstance(b, Vector):
            if len(self) != len(b):
                raise ValueError('dimensions must agree')
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = self[i] * b[i]
            return result
                
    def __rmul__(self, b): # function called if first operand does not support the corresponding operation
        try:
            if isinstance(b, (int, float)):
                result = Vector(len(self))
                for i in range(len(self)):
                    result[i] = self[i] * b
                return result
        except TypeError:
            raise TypeError('multiplier has to be an integer or float')
            
    
    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other   # rely on existing __eq__ definition

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation - without list brackets ([])

    def __neg__(self):
        """Return copy of vector with all coordinates negated."""
        result = Vector(len(self))           # start with vector of zeros
        for j in range(len(self)):
            result[j] = -self[j]
        return result

    def __lt__(self, other):
        """Compare vectors based on lexicographical order."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords < other._coords

    def __le__(self, other):
        """Compare vectors based on lexicographical order."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords <= other._coords


if __name__ == '__main__':
    # the following demonstrates usage of a few methods
    v = Vector(5)         # construct five-dimensional <0, 0, 0, 0, 0>
    v[1] = 23        # <0, 23, 0, 0, 0> (based on use of __setitem__)
    v[-1] = 45          # <0, 23, 0, 0, 45> (also via __setitem__)
    print(v[4])                # print 45 (via __getitem__)
    u = v + v                  # <0, 46, 0, 0, 90> (via __add__)
    print(u)                   # print <0, 46, 0, 0, 90>
    v_v = Vector([2, 'a'])
    print(v_v)
    
    v = [5, 3, 10, -2, 1] + u # to check if list can be concatated to vector
    total = 0
    print(v)
    print(v*3)
    print(3*v)
    print(v*u)
    for entry in v:
        total += entry
    print(total)  
