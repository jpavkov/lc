"""
930. Binary Subarrays With Sum
Medium
Topics: Array, Hash Table, Sliding Window, Prefix Sum

Given a binary array nums and an integer goal, return the 
number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

Example 1:
Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Example 2:
Input: nums = [0,0,0,0,0], goal = 0
Output: 15

Constraints:
    1 <= nums.length <= 3 * 104
    nums[i] is either 0 or 1.
    0 <= goal <= nums.length
"""


class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:

        ans = 0
        prefixSum = {}
        cumSum = 0

        for n in nums:
            cumSum += n
            if cumSum == goal:
                ans += 1
            if cumSum - goal in prefixSum:
                ans += prefixSum[cumSum - goal]
            prefixSum[cumSum] = prefixSum.get(cumSum, 0) + 1

        return ans


sol = Solution()


# ex 1: output: 4
nums = [1, 0, 1, 0, 1]
goal = 2
print(sol.numSubarraysWithSum(nums, goal))


# ex 2: output: 15
nums = [0, 0, 0, 0, 0]
goal = 0
print(sol.numSubarraysWithSum(nums, goal))
