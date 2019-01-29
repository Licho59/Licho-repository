from stack_class import Stack

def type_ch(x):
    try:
        int(x)
        return True
    except:
        return False
        

def infixToPostfix(infixexpr):
    prec = {}
    prec["^"] = 4 # exponentiation has priority before multiply and divide operations
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

            
    while ' ' in tokenList:
        tokenList.remove(' ')

    print(tokenList)    

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or type_ch(token):
            postfixList.append(token)
        elif len(token) > 1:
            print("KeyError in expression", infixexpr, " - bracket linked to operand")
            break
            
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
                    (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

if __name__ == '__main__':
    '''print(infixToPostfix("A * B + C * D"))
    print(infixToPostfix("(A + B ) * C - ( D - E ) * ( F + G )"))
    print(infixToPostfix("( A + B ) * ( C + D )"))
    print(infixToPostfix("( A + B ) * C"))
    print(infixToPostfix("A + B * C"))
    print(infixToPostfix("2 * 5 + 3 * 5 / ( 4 * 4 - 4 )"))
    print(infixToPostfix("( A + B ) * ( C + D ) * ( E + F )"))
    print(infixToPostfix("A + ( ( B + C ) * ( D + E ) )"))
    print(infixToPostfix("A * B * C * D + E + F"))'''
    print(infixToPostfix("15 * 3 ^ (4 - 2 )"))
