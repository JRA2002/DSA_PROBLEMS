'''You are given an m x n integer grid accounts where accounts[i][j] is 
the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the 
wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank 
accounts. The richest customer is the customer that has the maximum wealth.'''

def maximum_wealth(accounts):
        wealth = sum(accounts[0])

        for i in range(1, len(accounts)):
            if sum(accounts[i]) > wealth:
                wealth = sum(accounts[i])
        return wealth

accounts = [[1,2,3],[3,2,1]]
res = maximum_wealth(accounts)
print(res)

# Time Complexity:O(N*M)
# Auxiliary Space: O(1)