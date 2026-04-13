def BuySell1(prices):
    left = 0
    right = 1
    max_price = 0
    while right < len(prices) :
        profit = prices[right] - prices[left]
        if profit > max_price:
            max_price = profit
        elif profit < 0:
            left = right
        right += 1
    print(max_price)
    return max_price

prices = [7,1,5,3,6,4]
BuySell1(prices)