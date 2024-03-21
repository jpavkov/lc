"""
You are given an integer array prices where prices[i] 
is the price of a given stock on the ith day, and an 
integer k.

Find the maximum profit you can achieve. You may complete 
at most k transactions: i.e. you may buy at most k times 
and sell at most k times.

Note: You may not engage in multiple transactions 
simultaneously (i.e., you must sell the stock before you 
buy again).

Example 1:
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

Constraints:
    1 <= k <= 100
    1 <= prices.length <= 1000
    0 <= prices[i] <= 1000
"""

class Solution:

    def maxProfit(self, k: int, prices: list[int]) -> int:

        def dp(day, holding, remaining, depth):
            global call_count
            call_count += 1
            print(f"call count: {call_count}, day: {day}, holding: {holding}, remaining: {remaining}, depth: {depth}")

            if day == len(prices) or remaining == 0:
                return 0

            # do nothing
            ans = dp(day + 1, holding, remaining, depth + 1)

            # transaction
            if holding:
                # sell
                ans = max(ans, prices[day] + dp(day + 1, False, remaining - 1, depth + 1))
            else:
                # buy
                ans = max(ans, -prices[day] + dp(day + 1, True, remaining, depth + 1))

            # return the ans
            return ans

        # calls = 0
        
        ans = dp(0, False, k, 0)
        return ans

sol = Solution()
call_count = 0

k = 2
prices = [2,4,1]
print(sol.maxProfit(k, prices))

# k = 2
# prices = [3,2,6,5,0,3]
# print(sol.maxProfit(k, prices))

# k = 2
# prices = [3,3,5,0,0,3,1,4]
# print(sol.maxProfit(k, prices))
