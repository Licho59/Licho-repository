from queue_class import Queue
import random


def hotPotato(namelist):
    '''Returns last item which is still in queue after some number of "deque and enqueue'moves of item being in front of queue; at the end of each 'num times' cycle the first item in queue is being removed from the process(game)'''
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    playersize = len(namelist)

    while simqueue.size() > 1:
        num = random.randint(2, playersize*3)
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        name = simqueue.dequeue()
        print(name)

    return simqueue.dequeue()
    

def readInput():
    print("Enter player names, comma separated")
    names = input()
    '''while True:
        num = input("Enter count: ")
        if num.isdigit():
            num = int(num)
            break
        else:
            print("Bad Input. Please try again.")'''
    name_list = names.split(",")
    name_list = [n.strip() for n in name_list]
    return (name_list)


def main():
    players = readInput()
    winner = hotPotato(players)
    print("Winner is: ", winner)

if __name__ == '__main__':
    main()
