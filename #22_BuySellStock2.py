def BuySell2(prices):
    left = 0
    right = 1
    max_price = 0
    while right < len(prices):
        profit = prices[right] - prices[left]
        if profit > 0:
            max_price += profit
            left += 1
        else:
            left = right
        right += 1
    print(max_price)
    return(max_price)
    
prices = [7,1,5,3,6,4]
BuySell2(prices)