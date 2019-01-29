def anagramSolution1(s1, s2):
    '''That algoritm is O(n**2) order of magnitude.'''
    stillOK = True
    if len(s1) != len(s2):
        stillOK = False

    aList = list(s2)
    pos1 = 0
    while pos1 < len(s1) and stillOK:
        found = False
        pos2 = 0
        while pos2 < len(aList) and not found:
            if s1[pos1] == aList[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
        if found:
            aList[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK
    

def anagramSolution2(s1, s2):
    '''That algorithm is not O(n) even if it looks like becasue two sorting algorithms also account (either O(n**2) or O(nlogn).'''
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches
    

def anagramSolution3(s1, s2):
    '''That algorithm has a linear order of magnitude O(n) for solving this problem, so it is the best solution. It's vice is hovewer the additional memory space needed for storing both counting lists (c1, c2) but luckily they are not long - 26 is much less than for example million letter's alphabet :)'''
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j < 26 and stillOK:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK


print(anagramSolution1('abcd', 'dcba'))
print(anagramSolution2('cdefag', 'cdegak'))
print(anagramSolution3('apple', 'pleap'))
