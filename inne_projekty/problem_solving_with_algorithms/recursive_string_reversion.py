'''Write a function that takes a string as a parameter and returns a new string that is the reverse of the old string.'''


def testEqual(expression, exp):
    if expression == None:
        print("The expression is empty")
    if expression == exp:
        print("passed")


def reversedString(expression):
    temp = expression
    if temp == "":
        return None

    if len(temp) == 1:
        return str(temp)
    else:
        return reversedString(temp[1:]) + str(temp[0])
        
def reversedList(expression):
    temp = expression
    if temp == []:
        return None
    if len(temp) == 1:
        return temp
    else:
        return reversedList(temp[1:]) + list(temp[0])


print(reversedList(['a', 'b', 'c', 'd']))
'''print(reversedString('abcd'))

testEqual(reversedString("hello"), "olleh")
testEqual(reversedString("l"), "l")
testEqual(reversedString("follow"), "wollof")
testEqual(reversedString(""), "")'''
