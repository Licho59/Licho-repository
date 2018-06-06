from stack_class import Stack


def type_ch(x):
    try:
        int(x)
        return True
    except:
        return False


def infixToPostfix(infixexpr):
    prec = {}
    prec["^"] = 4  # exponentiation has priority before multiply and divide operations
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

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or type_ch(token):
            postfixList.append(token)
        elif len(token) > 1:
            print("KeyError in expression", infixexpr,
                  " - bracket linked to operand")
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
    

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if type_ch(token):
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
    return operandStack.pop()


def doMath(op, op1, op2):
    if op == "^":
        return op1 ** op2
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


if __name__ == '__main__':
    data1 = "15 * 3 ^ ( 4 - 2 )"
    postfix_exp = infixToPostfix(data1)
    print(postfix_exp)
    result = postfixEval(postfix_exp)
    print(result)
