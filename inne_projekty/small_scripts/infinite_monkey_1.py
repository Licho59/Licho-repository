import random

def generate_text(strlen):
    alphabet = ' abcdefghijklmnopqrstuvwxyz'
    res = ''
    for i in range(strlen):
        res += random.choice(alphabet)
    return res

def score(goal, teststring):
    numSame = 0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            numSame += 1
    return numSame / len(goal)
    
def main():
    goal_string = 'methinks it is a weasel'
    new_string = generate_text(28)
    best = 0
    n = 0
    new_score = score(goal_string, new_string)
    while new_score < 1:
        n += 1
        if new_score > best:
            best = new_score
        if n % 100000 == 0:
            print(best, new_string)
            
        new_string = generate_text(28)
        new_score = score(goal_string, new_string)
     
main()
