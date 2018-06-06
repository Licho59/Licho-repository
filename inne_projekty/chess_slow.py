
def queensAttack(n, k, r_q, c_q, obstacles):
    queen = (r_q - 1) * n + c_q
    result, numbers, bad_num = [], [], []

    for k in obstacles:
        bad_num.append((k[0] - 1) * n + k[1])
    # Counting for row
    for i in range(1, n + 1):
        numbers.append((r_q - 1) * n + i)
    for obs_num in bad_num:
        if obs_num in numbers and obs_num < queen:
            numbers = numbers[numbers.index(obs_num + 1):]
            numbers.remove(queen)
        elif obs_num in numbers and obs_num > queen:
            numbers = numbers[:numbers.index(obs_num)]
            numbers.remove(queen)
    if queen in numbers:
        numbers.remove(queen)
    result.extend(numbers)
    numbers = []

    # Counting for column
    for j in range(1, n + 1):
        numbers.append((j - 1) * n + c_q)
    for obs_num in bad_num:
        if obs_num in numbers and obs_num < queen:
            numbers = numbers[numbers.index(obs_num + 5):]
            numbers.remove(queen)
        elif obs_num in numbers and obs_num > queen:
            numbers = numbers[:numbers.index(obs_num)]
            numbers.remove(queen)
    if queen in numbers:
        numbers.remove(queen)
    result.extend(numbers)
    numbers = []

    # Counting for diagonals
    count_d = min(r_q - 1, c_q - 1)
    count_u = min((n - r_q), (n - c_q))

    for i in range(count_d + 1):
        numbers.append(queen - (n + 1) * i)
        if queen in numbers:
            numbers.remove(queen)
    for i in range(count_u + 1):
        numbers.append(queen + (n + 1) * i)
        if queen in numbers:
            numbers.remove(queen)
    for obs_num in bad_num:
        if obs_num in numbers and obs_num < queen:
            numbers = numbers[numbers.index(obs_num + 1):]
            numbers.remove(queen)
        elif obs_num in numbers and obs_num > queen:
            numbers = numbers[:numbers.index(obs_num)]
            numbers.remove(queen)
    if queen in numbers:
        numbers.remove(queen)
    result.extend(numbers)
    numbers = []

    count_d = min(r_q - 1, n - c_q)
    count_u = min(n - r_q, c_q - 1)
    for i in range(count_d + 1):
        numbers.append(queen - (n - 1) * i)
        if queen in numbers:
            numbers.remove(queen)
    for i in range(count_u + 1):
        numbers.append(queen + (n - 1) * i)
        if queen in numbers:
            numbers.remove(queen)
    for obs_num in bad_num:
        if obs_num in numbers and obs_num < queen:
            numbers = numbers[numbers.index(obs_num + 1):]
            numbers.remove(queen)
        elif obs_num in numbers and obs_num > queen:
            numbers = numbers[:numbers.index(obs_num)]
            numbers.remove(queen)
    if queen in numbers:
        numbers.remove(queen)
    result.extend(numbers)
    numbers = []

    return len(result)
    
if __name__ == "__main__":
    n, k = 4, 0
    r_q, c_q = 4, 4
    obstacles = []
    
    '''n, k = input().strip().split(' ')
    n, k = [int(n), int(k)] # n - size of board, k - number of obstacles
    r_q, c_q = input().strip().split(' ')
    r_q, c_q = [int(r_q), int(c_q)] # position of queen (numbers from 1 to n)
    obstacles = [] # positions of obstacles in [r_, c_]
    for obstacles_i in range(k):
       obstacles_t = [int(obstacles_temp)
                      for obstacles_temp in input().strip().split(' ')]
       obstacles.append(obstacles_t)'''
    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)
