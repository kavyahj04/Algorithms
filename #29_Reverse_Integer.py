def reverseInteger(x):
    q, r = 0, 0
    s = ""
    sol = 0
    negative = x < 0
    if x == 0:
        print(0)
        return 0
    elif negative:
        x = -x
    
    while x != 0:
        r = x % 10
        x = x // 10
        s+= str(r)

    if negative:
        sol = -int(s)
    else:
        sol = int(s)

    if sol < -2**31 or sol > 2**31 - 1:
        print(0)
        return 0
    else:
        print(sol)
        return sol

x = -123
reverseInteger(x)