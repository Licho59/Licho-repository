# Binary search tree - iterative search function
Key = 0
Left = 1
Right = 2
T = [8, [3, [1, [], []], [6, [4, [], []],
                          [7, [], []]]], [10, [], [14, [13, [], []], []]]]
def search(value, T):
    while T != []:
        print(T[Key])
        if T[Key] == value:
            return True
        elif T[Key] > value:
            T = T[Left]
        else:
            T = T[Right]
    return False

print(search(6, T))