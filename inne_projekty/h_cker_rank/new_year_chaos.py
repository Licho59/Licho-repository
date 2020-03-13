#! python
# new_year_chaos.py - from hackerrank.com - count the minimum number of bribes that took place to get the queue into its current state

# to improve because of run of time errors for data bigger than 10**3
def minimumBribes(q):
    count = 0
    q_ = [P - 1 for P in q]
    for i, P in enumerate(q_):
        if P - i > 2:
            print('Too chaotic')
            return
        else:
            for j in range(max(P-1,0), i):
                if q_[j] > P:
                    count += 1
    print(count)
    
    '''
    count = 0
    for i in range(len(q)):
        if q[i] - i > 3:
            print('Too chaotic')
            return 
        else: 
            if q[i] - i <= 1:
                c =len(list(filter(lambda x: x > q[i], q[q[i]-2:i])))
                count += c
    print(count)
 
    res = []
    for i in range(len(q)):
        res.append(q[i] - (i + 1))
    
    if max(res) > 2:
        print('Too chaotic')
    else:
        res = sorted([q[i] for i in range(len(q)) if (q[i] - (i + 1)) <= 0])
        count = 0
        for elm in res:
            dif = (q.index(elm) + 1 - elm)
            temp = q.pop(q.index(elm))
            q = q[:elm - 1] + [temp] + q[elm - 1:]
            count += dif
        print(count)

'''
f = open('Data/new_year_chaos_1.txt', 'r')
#f = open('Data/new_year_chaos_2.txt', 'r')
fs = f.readlines() # for 'data.txt' file: len(fs) = 13 - 1 (number of tests) + 6*2(n, testdata)
f.close()

fs = fs[0] 
q = [int(i) for i in fs.split(' ')]

#q = [1,2,5,3,7,8,6,4]
minimumBribes(q)
