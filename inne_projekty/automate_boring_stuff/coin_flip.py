#! python3
# 'coin_flip' - simulator of flipping coin, although to check debugging breakpoints

import random
heads = 0
for i in range(1, 1001):
    if random.randint(0,1) == 1:
        heads += 1
    if i == 500:
    # after marking the line as a breakpoint, program stops with actual heads number
        print('Halfway done!') 
print('Heads came up ' + str(heads) + ' times.')
