def DecodeString(s):
    stack = []
    i = 0
    while i < len(s):
        if s[i] == "]" :
            new_str = ""
            while stack and stack[-1] != "[":
                new_str = stack.pop() + new_str
            stack.pop()
            num = ""
            while stack and stack[-1].isdigit():
                num = stack.pop() + num
            num = int(num)
            stack.append(new_str * num)
            i += 1
        else:
            stack.append(s[i])
            i += 1
    print("".join(stack))
    return "".join(stack)

s = "2[abc]3[cd]ef"
DecodeString(s)
