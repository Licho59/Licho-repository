"""Draw a call stack for the Tower of Hanoi problem. Assume that you start with a stack of three disks."""

from stack_class import Stack

def hanoiStack(height, p_init, p_fin, p_temp):
    if height >= 1:
        hanoiStack(height-1, p_init, p_temp, p_fin)
        moveDisk(p_init, p_fin)
        hanoiStack(height-1, p_temp, p_fin, p_init)
    
def moveDisk(p_init, p_fin):
    global count
    disk = p_init.pop()
    p_fin.push(disk)
    count += 1
    print("moving " + str(disk) + " from " + str(p_init) + " to " + str(p_fin))
count = 0          
A = Stack()
B = Stack()
C = Stack()
for i in reversed(range(1,11)):
    A.push(i)

hanoiStack(10, A, B, C)
print("Number of moves: ", count)