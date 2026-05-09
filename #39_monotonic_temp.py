def monotonicTemp(temps):
    stack = []
    res = [0] * len(temps)

    for i, t in enumerate(temps):
        while stack and t > stack[-1][0]:
            stackT, stackI = stack.pop()
            res[stackI] = i - stackI
        stack.append([t, i])
    print(res)
    return res 

temperatures = [73,74,75,71,69,72,76,73]
monotonicTemp(temperatures)
