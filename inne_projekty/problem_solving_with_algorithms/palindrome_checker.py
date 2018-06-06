from pythonds.basic.deque import Deque
'''
Algorithm for checking if given string is palindrome or not; upgraded to version accepting spaces as blank characters.
'''
def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        while first == ' ':
            first = chardeque.removeFront()
        while last == ' ':
            last = chardeque.removeRear()
        
        if first != last:
            stillEqual = False

    return stillEqual


print(palchecker("lsdkjfskf"))
print(palchecker("radar"))
print(palchecker("I PREFER PI"))
