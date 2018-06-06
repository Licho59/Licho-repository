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


print(reversedString('abcd'))

testEqual(reversedString("hello"), "olleh")
testEqual(reversedString("l"), "l")
testEqual(reversedString("follow"), "wollof")
testEqual(reversedString(""), "")
