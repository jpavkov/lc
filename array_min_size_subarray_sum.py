"""
Given an array of positive integers nums and a positive 
integer target, return the minimal length of a subarray
whose sum is greater than or equal to target. If there 
is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length 
    under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:
    1 <= target <= 10^9
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^4
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        left = right = curr_sum = 0
        ans = 100001

        for num in nums:
            curr_sum += num
            right += 1
            while curr_sum >= target:
                ans = min(ans, right - left)
                curr_sum -= nums[left]
                left += 1

        return 0 if ans == 100001 else ans


sol = Solution()

# Example 1: Output: 2
target = 7
nums = [2, 3, 1, 2, 4, 3]
print(sol.minSubArrayLen(target, nums))

# Example 2: Output: 1
target = 4
nums = [1, 4, 4]
print(sol.minSubArrayLen(target, nums))

# Example 3: Output: 0
target = 11
nums = [1, 1, 1, 1, 1, 1, 1, 1]
print(sol.minSubArrayLen(target, nums))
