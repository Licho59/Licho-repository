def insertionSort(alist):
    '''Shifting operation in lines 10 and 11 makes algorithm better than those with exchange operations but it still is O(n**2).'''
    
    for index in range(1, len(alist)):
        current_value = alist[index]
        position = index
        
        # for every step in range scope one item from the list will be shifted to insert in correct place in ordering process
        while position > 0 and alist[position-1] > current_value:
            alist[position] = alist[position-1]
            position = position -1
        alist[position] = current_value
        
if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertionSort(alist)
    print(alist)
    