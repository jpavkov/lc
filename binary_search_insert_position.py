"""
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the 
index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:
    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums contains distinct values sorted in ascending order.
    -104 <= target <= 104
"""

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        if nums[right] < target:
            return right + 1
        if nums[left] > target:
            return 0

        while right - left > 1:
            midline = left + ((right - left) // 2)
            if nums[midline] >= target:
                right = midline
            else:
                left = midline

        if nums[right] >= target and nums[left] != target:
            return right
        return left

sol = Solution()

nums = [1,3]
target = 1
print(sol.searchInsert(nums, target))

nums = [1,3,5,6]
target = 5
print(sol.searchInsert(nums, target))

nums = [1,3,5,6]
target = 2
print(sol.searchInsert(nums, target))

nums = [1,3,5,6]
target = 7
print(sol.searchInsert(nums, target))


