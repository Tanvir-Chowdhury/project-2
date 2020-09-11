from pythonds.basic import Stack

def matches(open1, close):
    openers = "({["
    closers = ")}]"
    return openers.index(open1) == closers.index(close)

def perchecker(symbolstring):
    s = Stack()
    index = 0
    balanced = True
    while index < len(symbolstring):
        symbol = symbolstring[index]
        if symbol in "({[":
            s.push(symbol)
        else:
            top = s.pop()
            if not matches(top, symbol):
                balanced = False
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

print(perchecker('{({([][])}())}'))
print(perchecker('[{()]'))


        