"""
You are given an integer array cost where cost[i] is 
the cost of ith step on a staircase. Once you pay the 
cost, you can either climb one or two steps.

You can either start from the step with index 0, or 
the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
    - Pay 15 and climb two steps to reach the top.
    The total cost is 15.

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
    - Pay 1 and climb two steps to reach index 2.
    - Pay 1 and climb two steps to reach index 4.
    - Pay 1 and climb two steps to reach index 6.
    - Pay 1 and climb one step to reach index 7.
    - Pay 1 and climb two steps to reach index 9.
    - Pay 1 and climb one step to reach the top.
    The total cost is 6.

Constraints:
    2 <= cost.length <= 1000
    0 <= cost[i] <= 999
"""
class Solution:
    # recursive solution
    def minCostClimbingStairsTopDown(self, cost: list[int]) -> int:
        ## 1. a function that returns an answer
        def dp(i):
            if i <= 1:
                ## 3. base case
                return 0

            if i in memo:
                return memo[i]

            ## 2. recurrance relations
            memo[i] = min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])
            return memo[i]

        memo = {}
        return dp(len(cost))
    
    # iterative solution
    def minCostClimbingStairsBottomUp(self, cost: list[int]) -> int:
        
        n = len(cost)
        
        ## 2. create array that is sized according to the states
        dp = [0] * (n + 1)

        ## 3. base cases are implicit for 0 and 1

        ## 4. iterate over cases
        for i in range(2, n + 1):
            ## 5. each iteration of inner most loop represents a state
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        
        ## 6. return answer
        return dp[n]

sol = Solution()

cost = [10,15,20]
print(sol.minCostClimbingStairsTopDown(cost))
print(sol.minCostClimbingStairsBottomUp(cost))

cost = [1,100,1,1,1,100,1,1,100,1]
print(sol.minCostClimbingStairsTopDown(cost))
print(sol.minCostClimbingStairsBottomUp(cost))
