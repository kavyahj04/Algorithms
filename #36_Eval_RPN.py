def evaiRPN(tokens):
    stackTest = []
    for c in tokens:
        if c == "+":
            stackTest.append(stackTest.pop() + stackTest.pop())
        elif c == "-":
            a , b = stackTest.pop(), stackTest.pop()
            stackTest.append(int(b - a))
        elif c == "*":
            stackTest.append(stackTest.pop() * stackTest.pop())
        elif c == "/":
            a , b = stackTest.pop(), stackTest.pop()
            stackTest.append(int(b / a))
        else:
            stackTest.append(int(c))
    print(stackTest[0])   
    return stackTest[0]

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
evaiRPN(tokens)