import random
from queue_class import Queue

'''That algorithm for so called 'radix sorting machine' has been made on my own and it's working! For data it takes the list of numbers from given range - it should be upgraded to data being inputted by user.
'''

def putToMainBin(main_bin, numbers):
    while numbers:
        rand_num = random.choice(numbers)
        temp = numbers.pop(numbers.index(rand_num))
        main_bin.enqueue(temp)
    return main_bin.printQueue()


def putToSmallBins(main_bin, bins, n):
    while not main_bin.isEmpty():
        num = str(main_bin.dequeue())
        bins[int(num[n - 1])].enqueue(num)
    return bins


def collectBins(bins, main_bin):
    for elm in bins[:-1]:
        while not elm.isEmpty():
            main_bin.enqueue(elm.dequeue())
    return main_bin


def main():
    given_number = input('Give the number for creating the list with numbers up to given one: ')
    k = len(given_number)
    num = int(given_number)
    numbers = [('{i:0{width}}'.format(i=number, width=k)) for number in range(0, num)]
    biggest = str(max(numbers))
    n = len(biggest)
    main_bin = Queue()

    bins = []
    for i in range(10):
        bin_i = Queue()
        bins.append(bin_i)
    bins.append(main_bin)

    putToMainBin(main_bin, numbers)

    while n >= 1:
        putToSmallBins(main_bin, bins, n)
        collectBins(bins, main_bin)
        n -= 1
    print(main_bin.printQueue())
    '''while not main_bin.isEmpty():
        numbers.append(main_bin.dequeue())
    print(numbers)'''

    return main_bin


if __name__ == '__main__':
    main()
