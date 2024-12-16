'''The stock span problem is a financial problem where we have 
a series of N daily price quotes for a stock and we need to 
calculate the span of the stock’s price for all N days. 
The span Si of the stock’s price on a given day i is defined 
as the maximum number of consecutive days just before the given 
day, for which the price of the stock on the current day is less 
than or equal to its price on the given day. '''

def stock_span(arr):
    past = arr[0]
    print(1)
    for i in range(1, len(arr)):
        actual = arr[i]
        if past >= actual:
            print(1)
            #incomplete
        else:
            print(2)
        past = actual
arr = [100 ,80 ,60 ,70 ,60 ,75 ,85]
stock_span(arr)
