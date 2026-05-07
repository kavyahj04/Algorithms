def valid_Parenthesis(parenthesisList):
    stack = []
    closeToOpen = {")" : "(", "]" : "[", "}" : "{"}
    for c in parenthesisList:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                print("False")
                return False
        else:
            stack.append(c)
    print("True") if not stack else print("False")
    return True if not stack else False

s = "([)]"
valid_Parenthesis(s)