def shellSort(alist):
    '''The list is being more and more sorted so there is less number of comparisons(shifts) and its effectivness is around O(n**3/2)'''
    
    sublistcount = len(alist) // 2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist, startposition, sublistcount)

      #print("After increments of size", sublistcount,
       #     "The list is", alist)

      sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):

        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue

if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shellSort(alist)
    print(alist)
