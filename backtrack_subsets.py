"""
Given an integer array nums of unique elements, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the 
solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All the numbers of nums are unique.
"""

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def backtrack(curr, i: int):
            if i > len(nums):
                return
            ans.append(curr[:])

            for j in range(i, len(nums)):
                curr.append(nums[j])
                backtrack(curr, j + 1)
                curr.pop()

        ans = []
        backtrack([], 0)
        return ans


sol = Solution()

# Example 1, expected output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
nums = [1,2,3]
print(sol.subsets(nums))

# Example 2, expected output: [[],[0]]
nums = [0]
print(sol.subsets(nums))
