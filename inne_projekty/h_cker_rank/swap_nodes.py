idx = [[2, 3], [4, -1], [5, -1], [6, -1], [7, 8], [-1, 9],
       [-1, -1], [10, 11], [-1, -1], [-1, -1], [-1, -1]]
new_idx = [[],[1]]
# count for number of non -1 values in idx[i] array
c_1 = len([i for i in idx[0] if i != -1])
new_idx.append(idx[0])
idx.pop(0)
while len(idx) > 0:
    temp = []
    for i in range(c_1):
        temp.append(idx[i])
    del idx[:c_1]
    c_1 = len([temp[i][j] for i in range(len(temp))
               for j in range(2) if temp[i][j] != -1])
    new_idx.append(temp)

for elm in new_idx:
    print(elm, '\n')

depth = len(new_idx)
s = [2,4]

for lev in s:
    while lev <= depth:
        for l in new_idx[lev+1]:
            l.reverse()
        lev += lev
    print(new_idx[1:-1])    
        