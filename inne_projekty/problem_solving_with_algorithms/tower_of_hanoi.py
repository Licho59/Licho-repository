import time

count = 0

def moveTower(height, fromPole, toPole, withPole):
    global count
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        count += 1
        moveDisk(fromPole, toPole)
        moveTower(height - 1, withPole, toPole, fromPole)


def moveDisk(fp, tp):
    global count
    print(count, "- moving disk from", fp, "to", tp)

t1 = time.time()
moveTower(3, "A", "B", "C")
t2 = time.time()
print("The total number of moves is " + str(count))
print("It took ", str(round((t2-t1) ,3)), "seconds")
