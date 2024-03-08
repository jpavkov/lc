"""
Given an integer array nums and an integer k, 
split nums into k non-empty subarrays such 
that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.

Example 1:
Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
    The best way is to split it into [7,2,5] and [10,8], 
    where the largest sum among the two subarrays is only 18.

Example 2:
Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
    The best way is to split it into [1,2,3] and [4,5], 
    where the largest sum among the two subarrays is only 9.

Constraints:
    1 <= nums.length <= 1000
    0 <= nums[i] <= 106
    1 <= k <= min(50, nums.length)
"""

class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        
        def min_subarrays_required(max_sum_allowed: int) -> int:
            current_sum = 0
            splits_required = 0
            for element in nums:
                if current_sum + element <= max_sum_allowed:
                    current_sum += element
                else:
                    current_sum = element
                    splits_required += 1

            return splits_required + 1

        left = max(nums)
        right = sum(nums)
        while left <= right:
            max_sum_allowed = (left + right) // 2
            m_subs = min_subarrays_required(max_sum_allowed)
            if m_subs <= k:
                right = max_sum_allowed - 1
                minimum_largest_split_sum = max_sum_allowed
            else:
                left = max_sum_allowed + 1

        return minimum_largest_split_sum

# run solution
sol = Solution()

# # use case 1
# nums = [7,2,5,10,8]
# k = 2
# print(sol.splitArray(nums, k))  # 18

# # use case 2
# nums = [1,2,3,4,5]
# k = 2
# print(sol.splitArray(nums, k))  # 9

# # use case 3
# nums = [7,2,5,6,8,4,3]
# k = 3
# print(sol.splitArray(nums, k))  # 14

# use case 4
nums = [1,4,4]
k = 3
print(sol.splitArray(nums, k))  # 4
