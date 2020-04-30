# Examples of using asterisks in Python



# 1. Astersks for unpacking into function call (instead of indexing of each element
fruits = ['lemon', 'pear', 'watermelon', 'tomato']
# without asterisks you need to index each element of iterable object
print(fruits[0], fruits[1], fruits[2], fruits[3])

# by passing all of the items of 'fruits' iterable into print() function call as
# separate arguments (no need to know how many of arguments are in the list)
print(*fruits)
print('-'*30)

# another example - list of lists is unpacked into separate elements or transposed
# into another list of list
comp_list = [[1,4,7],[2,5,8],[3,6,9]]
a, b, c = (zip(*comp_list))
print(a), print(b), print(c)
print(list(zip(*comp_list)))
print('-'*30)

# '**' asteriks for working with keyword arguments - unpacking dict keys
date_info = {'year': '2020', 'month': '01', 'day': '01'}
filename = "{year}-{month}-{day}.txt".format(**date_info)
print(filename)
print('-'*30)

# similar example
date_info = {'year': "2020", 'month': "01", 'day': "01"}
track_info = {'artist': "Beethoven", 'title': 'Symphony No 5'}
filename = "{year}-{month}-{day}-{artist}-{title}.txt".format(
                                                    **date_info, **track_info)
print(filename)
print('-'*30)

# 2. Asterisks for packing arguments given to function
from random import randint

def roll(*dice):
    return sum(randint(1, die) for die in dice)

# roll() function works with any number of arguments
print(roll(10))
print(roll(1,23))
print(roll(4,5,8,12,90))
print('-'*30)

# usefule with print() and zip() functions
m = [2,3,4,5,6]
n = [20,30,40]
print(*m, *n, sep='~')
print(list(zip(m, n)))
print('-'*30)

# example of tag() function with any number of keyword arguments
def tag(tag_name, **attributes):
    attribute_list = [
        f'{name}="{value}"'
        for name, value in attributes.items()
    ]
    return f"<{tag_name} {' '.join(attribute_list)}>"

print(tag('img', height=20, width=40, src="face.jpg"))
print(tag('a', href="http://treyhunner.com"))
