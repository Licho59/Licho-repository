'''Write a program that solves the following problem: Three missionaries and three cannibals come to a river and find a boat that holds two people. Everyone must get across the river to continue on the journey. However, if the cannibals ever outnumber the missionaries on either bank, the missionaries will be eaten. Find a series of crossings that will get everyone safely to the other side of the river.'''
men_before = 3
cannibals_before = 3
boat = 0
men_after = 0
cannibals_after = 0
crosses = []
while (men_before or cannibals_before):
    if men_after == cannibals_after == 0:
        cannibals_before -= 1
        cannibals_after += 1
        crosses.append('C+C')
        crosses.append('C_back')
    elif cannibals_after > men_after:
        men_before -= 1
        men_after += 1
        crosses.append('M+C')
        crosses.append('C_back')
    elif cannibals_after == men_after != 0:
        men_before -= 2
        men_after += 2
        crosses.append('M+M')
        crosses.append('C_back')
    elif men_after > cannibals_after:
        cannibals_before -= 1
        cannibals_after += 1
        crosses.append('C+M')
        crosses.append('C_back')


print("Number of courses:", len(crosses), crosses)
