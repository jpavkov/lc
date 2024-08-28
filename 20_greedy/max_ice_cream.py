# https://leetcode.com/problems/maximum-ice-cream-bars/description/

class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()

        for i, num in enumerate(costs):
            if coins >= num:
                coins -= num
            else:
                return i

        return len(costs)


sol = Solution()
costs = [1, 3, 2, 4, 1]
coins = 7
print(sol.maxIceCream(costs, coins))

costs = [10, 6, 8, 7, 7, 8]
coins = 5
print(sol.maxIceCream(costs, coins))

costs = [1, 6, 3, 1, 2, 5]
coins = 20
print(sol.maxIceCream(costs, coins))
