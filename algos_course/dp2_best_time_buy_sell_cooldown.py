"""
You are given an array prices where prices[i] 
is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You 
may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock 
multiple times) with the following restrictions:
    After you sell your stock, you cannot buy 
        stock on the next day (i.e., cooldown 
        one day).
    Note: You may not engage in multiple 
        transactions simultaneously (i.e., you 
        must sell the stock before you buy again).

Example 1:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:
Input: prices = [1]
Output: 0

Constraints:
    1 <= prices.length <= 5000
    0 <= prices[i] <= 1000
"""

from functools import cache

class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        @cache
        def dp(i, hold):

            if i >= len(prices):
                return 0
            
            ans = dp(i + 1, hold)

            if hold is False:
                ans = max(ans, dp(i + 1, True) - prices[i])
            else:
                ans = max(ans, dp(i + 2, False) + prices[i])
            
            return ans

        ans = dp(0, False)
        return ans

sol = Solution()

# example 1, ans: 3
prices = [1,2,3,0,2]
print(sol.maxProfit(prices))

# example 2, ans: 0
prices = [1]
print(sol.maxProfit(prices))
