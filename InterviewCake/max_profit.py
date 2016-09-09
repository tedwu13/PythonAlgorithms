
# O(n^2)
def max_profit(stock_prices_yesterday):
    max_profit = 0

    for i in xrange(len(stock_prices_yesterday)):
        for j in xrange(len(stock_prices_yesterday)):
            buy_time = min(i, j)
            sell_time = max(i,j)

            buy_price = stock_prices_yesterday[buy_time]
            sell_price = stock_prices_yesterday[sell_time]

            potential_profit = sell_price - buy_price

            max_profit = max(potential_profit, max_profit)

    return max_profit



# keep track of the lowest price
# check if you can have a bigger profit 
def max_profit(stock_prices_yesterday):
    max_profit = 0
    min_price = stock_prices_yesterday[0]
    for current_price in stock_prices_yesterday: 
        min_price = min(min_price, current_price)
        profit = current_price - min_price
        max_profit = max(max_profit, profit)
    return max_profit

# one of the edge case is if the prices keep going down, then we will return max_profit = 0
def max_profit(stock_prices_yesterday):
    max_profit = 0
    min_price = stock_prices_yesterday[0]
    for current_price in stock_prices_yesterday: 
        min_price = min(min_price, current_price)
        profit = current_price - min_price
        max_profit = max(max_profit, profit)
    return max_profit


