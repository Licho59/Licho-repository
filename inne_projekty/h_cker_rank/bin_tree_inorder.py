# Binary tree - orderingi function
T = [2, [7, [2, [], []], [6, [5, [], []],
                          [11, [], []]]], [5, [], [9, [4, [], []], []]]]
Key = 0
Left = 1
Right = 2

def inorder(T):
    if T != []:
        inorder(T[Left])
        print(T[Key]), inorder(T[Right])

inorder(T)