'''Write a program to solve the following problem: You have two jugs: a 4-gallon jug and a 3-gallon jug. Neither of the jugs have markings on them. There is a pump that can be used to fill the jugs with water. How can you get exactly two gallons of water in the 4-gallon jug?'''


def fill_water(big, small, task):
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
    big_jug_place = big
    big_jug += small_jug
    print(big_jug)


fill_water(4, 3, 2)
