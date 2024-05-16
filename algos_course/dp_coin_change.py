"""
You are given an integer array coins representing 
coins of different denominations and an integer 
amount representing a total amount of money.

Return the fewest number of coins that you need to 
make up that amount. If that amount of money cannot 
be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of 
each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Constraints:
    1 <= coins.length <= 12
    1 <= coins[i] <= 231 - 1
    0 <= amount <= 104
"""
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        
        def dp(remaining):
            # Check if the result is already memoized
            if remaining in memo:
                return memo[remaining]
            if remaining < 0:
                return -1
            if remaining == 0:
                return 0
            min_cost = 10001 #float('inf')
            for coin in coins:
                result = dp(remaining - coin)
                if result != -1:
                    min_cost = min(min_cost, result + 1)
            # Memoize the computed result before returning
            memo[remaining] = min_cost if min_cost != 10001 else -1 #float('inf')
            return memo[remaining]

        memo = {}
        return dp(amount)


sol = Solution()

# example 1, output: 3
coins = [1,2,5]
amount = 11
print(sol.coinChange(coins, amount))

# example 2, output: -1
coins = [2]
amount = 3
print(sol.coinChange(coins, amount))

# example 3, output: 0
coins = [1]
amount = 0
print(sol.coinChange(coins, amount))
