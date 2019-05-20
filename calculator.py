def main():

    inputCommand = input('Which math operation you want to do? (+) (-) (*) (/) (sq) (sqroot)')

    if inputCommand.lower() not in ('+','-','*','/','sq','sqroot'):
        inputCommand = input('Incorrect input. Please select one of them before typing: (+) (-) (*) (/) (sq) (sqroot)')

    elif inputCommand in ('+', '-', '*', '/'):
        firstNum = input('First number:')
        while isFloat(firstNum) != 1 and isInteger(firstNum) != 1:
            firstNum = input('Incorrect format, please write with numbers (eg: 1 or 1.5)')
        if isInteger(firstNum) == 1: firstNum = int(firstNum)
        else: firstNum=float(firstNum)

        secondNum = float(input('Second number:'))
        while isFloat(secondNum) != 1 and isInteger(secondNum) != 1:
            secondNum = input('Incorrect format, please write with numbers (eg: 1 or 1.5)')
        if isInteger(secondNum) == 1: secondNum=int(secondNum)
        else: secondNum=float(secondNum)


        if inputCommand == '+':
            print(sumof(firstNum, secondNum))
        elif inputCommand == '-':
            print(subsof(firstNum, secondNum))
        elif inputCommand == '*':
            print(multiply(firstNum, secondNum))
        elif inputCommand == '/':
            print(divide(firstNum, secondNum))

    elif inputCommand in ('sq', 'sqroot'):
        firstNum = input('Your number:')
        while isFloat(firstNum) != 1 and isInteger(firstNum) != 1:
            firstNum = input('Incorrect format, please write with numbers (eg: 1 or 1.5)')
        if isInteger(firstNum) == 1: firstNum = int(firstNum)
        else: firstNum=float(firstNum)
        if inputCommand == 'sq':
            print(sq(firstNum))
        elif inputCommand == 'sqroot':
            print(sqroot(firstNum))

def sumof(x, y):
    return x + y
def subsof(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def sq(x):
    return x ** 2
def sqroot(x):
    return x ** (1 / 2)

def isInteger(x):
    try:
        int(x)
        return True
    except:
        return False


def isFloat(x):
    try:
        float(x)
        return True
    except:
        return False



activate = 1
while activate:
    main()
    continueQuestion = input('Do you want to continue? (Y/N)')
    while continueQuestion.lower() not in ('n','y'):
        continueQuestion = input('Wrong input! Do you want to continue? (Y/N)')
    if continueQuestion.lower() == 'n':
        activate = 0
