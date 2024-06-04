"""
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in 
non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:
    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in non-decreasing order.
"""


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:

        left = 0
        right = len(nums) - 1
        pointer = len(nums) - 1
        ans = [0] * (right + 1)

        while pointer >= 0:
            if abs(nums[left]) > nums[right]:
                ans[pointer] = nums[left] ** 2
                left += 1
            else:
                ans[pointer] = nums[right] ** 2
                right -= 1
            pointer -= 1

        return ans


sol = Solution()

nums = [-4, -1, 0, 3, 10]
print(sol.sortedSquares(nums))

nums = [-7, -3, 2, 3, 11]
print(sol.sortedSquares(nums))
