'''Generalize the problem solved in '4_3_liter_jugs.py" so that the parameters to your solution include the sizes of each jug and the final amount of water to be left in the larger jug.'''

def fill_water(big, small, task):
    count = 0
    big_jug_place = big
    small_jug = small
    big_jug = 0
    while small_jug != task:
        if big_jug_place > small:
            big_jug_place -= small_jug
            small_jug = small
        else:
            small_jug = small - big_jug_place
            big_jug_place = big
        count += 1
        if count > big:
            return "The task impossible to realize"
    big_jug_place = big
    big_jug += small_jug
    return "The task completed - in large jug is " + str(big_jug) + " litres of water"

big = int(input("Give a natural number for big jug volume: "))
small = int(input("Give a natural number for small jug volume: "))
task = int(input("Give a number for amount of water to be left in larger jug: "))


print(fill_water(big, small, task))
