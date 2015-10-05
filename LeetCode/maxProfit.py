def maxProfit(prices):
    maximum_price = 0
    minimum_price = float("infinity")
    max_profit = 0

    for price in prices:
        if price < 0:
            print "No negative prices"
        minimum_price = min(minimum_price, price)
        max_profit = max(max_profit, price - minimum_price)
    return max_profit
    
print maxProfit([3,2,1,4,2,5,6])

