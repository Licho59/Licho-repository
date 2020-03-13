# Binary search tree (BST) - iterative search and insert functions
Key = 0
Left = 1
Right = 2
T = [8, [3, [1, [], []], [6, [4, [], []],
                          [7, [], []]]], [10, [], [14, [13, [], []], []]]]

def search(value, T):
    while T != []:
        node = T
        if T[Key] > value:
            T = T[Left]
        else:
            T = T[Right]
    return node

def insert(value, T):
    parent = search(value, T)
    node = [value, [], []]
    if parent[Key] > value:
        parent[Left] = node
    else:
        parent[Right] = node

print(search(10, T))
print(insert(10, T))