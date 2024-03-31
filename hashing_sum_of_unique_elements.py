"""
You are given an integer array nums. The unique elements of an 
array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.

Example 1:
Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.

Example 2:
Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.

Example 3:
Input: nums = [1,2,3,4,5]
Output: 15
Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.

Constraints:
    1 <= nums.length <= 100
    1 <= nums[i] <= 100
"""


class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:

        seen = {}
        ans = 0

        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        for key, value in seen.items():
            if value == 1:
                ans += key

        return ans


sol = Solution()

# ex 1: output: 4
nums = [1, 2, 3, 2]
print(sol.sumOfUnique(nums))

# ex 2: output: 0
nums = [1, 1, 1, 1, 1]
print(sol.sumOfUnique(nums))

# ex 3: output 15
nums = [1, 2, 3, 4, 5]
print(sol.sumOfUnique(nums))
