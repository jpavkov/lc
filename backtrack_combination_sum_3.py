"""
Find all valid combinations of k numbers that sum up 
to n such that the following conditions are true:
    Only numbers 1 through 9 are used.
    Each number is used at most once.
Return a list of all possible valid combinations. The 
list must not contain the same combination twice, and 
the combinations may be returned in any order.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation: 
    1 + 2 + 4 = 7
    There are no other valid combinations.

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
    1 + 2 + 6 = 9
    1 + 3 + 5 = 9
    2 + 3 + 4 = 9
    There are no other valid combinations.

Example 3:
Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
    Using 4 different numbers in the range [1,9], the 
    smallest sum we can get is 1+2+3+4 = 10 and since 
    10 > 1, there are no valid combination.

Constraints:
    2 <= k <= 9
    1 <= n <= 60
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:

        def backtrack(cur_nums):
            if sum(cur_nums) == n and len(cur_nums) == k:
                ans.append(list(cur_nums))
                return

            if sum(cur_nums) > n or len(cur_nums) == k:
                return

            start_range = 0 if not cur_nums else max(cur_nums)
            for i in range(start_range, 9):
                cur_nums.append(i + 1)
                backtrack(cur_nums)
                cur_nums.pop()

        ans = []
        backtrack([])
        return ans


sol = Solution()
k = 3
n = 7
print(sol.combinationSum3(k, n))

k = 3
n = 9
print(sol.combinationSum3(k, n))

k = 4
n = 1
print(sol.combinationSum3(k, n))

