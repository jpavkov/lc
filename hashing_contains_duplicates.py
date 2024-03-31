"""
Given an integer array nums, return true if any value appears 
at least twice in the array, and return false if every element 
is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        setNums = set(nums)
        return len(setNums) != len(nums)


sol = Solution()

# Example 1: Output: true
nums = [1, 2, 3, 1]
print(sol.containsDuplicate(nums))

# Example 2: Output: false
nums = [1, 2, 3, 4]
print(sol.containsDuplicate(nums))

# Example 3: Output: true
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(sol.containsDuplicate(nums))
