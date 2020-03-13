# Binary search tree (BST) - min and max plus recursive search function
Key = 0
Left = 1
Right = 2
T = [8, [3, [1, [], []], [6, [4, [], []],
                          [7, [], []]]], [10, [], [14, [13, [], []], []]]]
def search(value, T):
    if T != []:
        print(T[Key])
        if T[Key] == value:
            return True
        elif T[Key] > value:
            return search(value, T[Left])
        else:
            return search(value, T[Right])
    else:
        return False

def minimum(T):
    if T[Left] != []:
        return minimum(T[Left])
    else:
        return T[Key]

def maximum(T):
    if T[Right] != []:
        return maximum(T[Right])
    else:
        return T[Key]

print(minimum(T), maximum(T))
#print(search(6, T))
