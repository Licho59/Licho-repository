"""
Simulation of river environment containing bears and fish.
"""

import random

class Animal:
    """Animals are the inhabitants of the river"""

    def __init__(self, gender=None, strength=None):
        """Initialize animal

        gender     gender of the animal(M, F) determines mating or fighting(default random)
        strength   stregth of animal, determines winner of fight(default random)
        """

        if not gender:
            self._gender = random.choice(['M','F'])
        else:
            self._gender = gender
        if not strength:
            self._strength = random.randint(0,9)
        else:
            self._strength = strength

    @property
    def gender(self):
        return self._gender

    @property
    def stren(self):
        return self._strength


class Bear(Animal):
    def __init__(self, gender = None, strength = None):
        super().__init__(gender, strength)

class Fish(Animal):
    def __init__(self, gender = None, strength = None):
        super().__init__(gender, strength)

class River:
    """A river is in array containing animals"""

    def __init__(self, length):
        """Initialize a river with a random assortment of bears, fish, and empty cells; length - length of the river
        """
        self._length = length
        self._contents = []
        animal_types = (Bear, Fish)
        len_animal_types = len(animal_types)
        
        for i in range(self._length):
            rval = random.randint(0, len_animal_types)
            if rval == len_animal_types:
                self._contents.append(None)
            else:
                self._contents.append(animal_types[rval]())
           

    def __len__(self):
        """Return the length of the river"""
        return self._length

    def __getitem__(self, k):
        """Return the contents of the kth cell in the river list"""
        return self._contents[k]

    def __setitem__(self, k, val):
        """Set the contents of the kth cell in the river list"""
        self._contents[k] = val

    def count_none(self):
        """Count the number of empty cells in the river list"""
        return self._contents.count(None)

    def add_random(self, animal):
        """Add animal to empty cell of river list after mating occurs"""
        if self.count_none() > 0:
            choices = [i for i, x in enumerate(self._contents) if x is None]
            index = random.choice(choices)
            self._contents[index] = animal

    def update_cell(self, i):
        """Update the cell based on rules defined above"""
        if self._contents[i] != None:
            #animal can either move forward, back, or stay in place
            move = random.randint(-1,1)
            if move != 0 and 0 <= i + move < self._length:
                if self._contents[i + move] is None:
                    self._contents[i + move] = self._contents[i]
                    self._contents[i] = None
                elif type(self._contents[i]) == type(self._contents[i+move]):
                    if self._contents[i].gender != self._contents[i+move].gender:
                        #two animals of the same type and different gender mate
                        if type(self._contents[i]) == Bear:
                            self.add_random(Bear())
                        else:
                            self.add_random(Fish())
                    else: #two animals of the same type and gender fight
                        if self._contents[i].stren > self._contents[i+move].stren:
                            self._contents[i+move] = self._contents[i]
                        self._contents[i] = None

                else:
                    #bear always kills fish if they encounter eachother
                    if type(self._contents[i]) == Bear:
                        self._contents[i + move] = self._contents[i]
                    self._contents[i] = None

    def update_river(self):
        """Update each cell in the river"""
        for i in range(len(self._contents)):
            self.update_cell(i)

    def print_river(self):
        """Print the river contents in human readable form
           Each cell displays the animal type, strength, and gender between two pipes

           Example: male bear with strength 8 | B8M|
                    female fish with strength 0 | F0F|
        """
        s = '|'
        for x in self._contents:
            if x:
                if type(x) == Bear:
                    s += 'B'
                elif type(x) == Fish:
                    s += 'F'
                s += str(x.stren)
                s += x.gender
            else:
                s += '   '
            s += '|'
        print(s)


if __name__ == "__main__":
    river = River(10)
    for i in range(10):
        print("Year ", i)
        river.print_river()
        river.update_river()
