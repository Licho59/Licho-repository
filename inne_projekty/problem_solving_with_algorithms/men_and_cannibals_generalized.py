'''Task from 'men_and_cannibals.py' has been upgraded to more generalized form - the number of men or cannibals - arbitrary.'''
men_before = 5
cannibals_before = 5
def menWithCannibalsInBoat(N):
    global count
    count = 0
    men_before = cannibals_before = N
    men_after = cannibals_after = 0
    crosses = []
    while men_before + cannibals_before > 2:
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
            men_before -= 1
            men_after += 1
            crosses.append('M+C')
            crosses.append('C_back')
        elif men_after > cannibals_after:
            cannibals_before -= 1
            cannibals_after += 1
            crosses.append('C+M')
            crosses.append('C_back')
        count += 2

    men_before -= 1
    men_after += 1
    cannibals_before -= 1
    cannibals_after += 1
    crosses.append('M+C')
    count += 1
    return crosses

N = 5
 
print(menWithCannibalsInBoat(N))
print("Number of crosses:", count)
