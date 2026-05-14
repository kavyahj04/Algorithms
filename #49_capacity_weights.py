def capCheck(c):
    sum_ = 0
    d = 1
    for i in range(len(weights)):
        if sum_ + weights[i] <= c:
            sum_ += weights[i]
        else:
            d = d+1
            sum_ = 0
            sum_ += weights[i]
    if d <= days:
        return True
    else:
        return False 