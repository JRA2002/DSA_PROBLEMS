'''You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.'''

def buy_sell_stocks(prices: list):
    l = 0
    r = 1
    n = len(prices) - 1
    maxP = 0
    while r <= n:
        if prices[l] > prices[r]:
            l = r
        maxP = max(maxP, prices[r] - prices[l])
        r += 1
    return maxP

# Time Complexity:O(N)
# Auxiliary Space: O(1)
    
# using dynamic programming
# most elegant solution
def buy_sell_stocks2(prices: list):
    maxP = 0
    minB = prices[0]
    for sell in prices:
        maxP = max(maxP, sell - minB)
        minB = min(minB, sell)

    return maxP


arr = [7,6,4,3,1]
res = buy_sell_stocks2(arr)
print(res)

# Time Complexity:O(N)
# Auxiliary Space: O(1)