"""
Given an integer array nums, return the length of 
the longest strictly increasing subsequence.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:
    1 <= nums.length <= 2500
    -104 <= nums[i] <= 104
"""

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        
        n = len(nums)

        def previousMax(i):
            v = max([(value) for key, value in memo.items() if 1 <= key < i])
            if v:
                return v
            return 0

        def dp(i):
            if i == 0:
                memo[nums[i]] = 1
                return
            
            memo[i] = 
            


        memo = {}
        return dp(n - 1)
    


