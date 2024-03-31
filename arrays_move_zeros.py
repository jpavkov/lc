"""
Given an integer array nums, move all 0's to the end of 
it while maintaining the relative order of the non-zero 
elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:

        if len(nums) == 1:
            return

        zeros = 0

        for i, num in enumerate(nums):
            if num == 0:
                zeros += 1
            elif zeros != 0:
                nums[i - zeros] = num

        if zeros > 0:
            nums[-zeros:] = [0] * zeros


sol = Solution()

nums = [0, 1, 0, 3, 12]
print(nums)
sol.moveZeroes(nums)
print(nums)

nums = [0]
print(nums)
sol.moveZeroes(nums)
print(nums)
