"""
Given two integers n and k, return all possible 
combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: 
    There are 4 choose 2 = 6 total combinations. 
    Note that combinations are unordered, i.e., 
        [1,2] and [2,1] are considered to be the 
        same combination.

Example 2:
Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

Constraints:
    1 <= n <= 20
    1 <= k <= n
"""

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:

        def backtrack(curr, i):
            if len(curr) == k:
                ans.append(curr[:])
                return

            for j in range(i, n + 1):
                if j not in curr:
                    curr.append(j)
                    backtrack(curr, j + 1)
                    curr.pop()

        ans = []
        backtrack([], 1)
        return ans

sol = Solution()

# example 1, expected output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
n = 4
k = 2
print(sol.combine(n,k))

# example 2, expected output: [[1]]
n = 1
k = 1
print(sol.combine(n,k))
