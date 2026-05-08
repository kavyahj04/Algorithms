def remove_All_adj_dup(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    print("".join(stack))
    return "".join(stack)

s = "abbaca"
remove_All_adj_dup(s)