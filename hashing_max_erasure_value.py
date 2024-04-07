"""
1695. Maximum Erasure Value
Medium
Topics: Array, Hash Table, Sliding Window

You are given an array of positive integers nums and want 
to erase a subarray containing unique elements. The score 
you get by erasing the subarray is equal to the sum of its 
elements.

Return the maximum score you can get by erasing exactly one 
subarray.

An array b is called to be a subarray of a if it forms a 
contiguous subsequence of a, that is, if it is equal to 
a[l],a[l+1],...,a[r] for some (l,r).

Example 1:
Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].

Example 2:
Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].

Constraints:
    1 <= nums.length <= 105
    1 <= nums[i] <= 104
"""


class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:

        dic = {}
        left = ans = 0

        for right, value in enumerate(nums):
            if value in dic:
                left = max(left, dic[value] + 1)
            dic[value] = right
            ans = max(ans, sum(nums[left:right + 1]))

        return ans


sol = Solution()


# ex 1: output: 17
nums = [4, 2, 4, 5, 6]
print(sol.maximumUniqueSubarray(nums))

# ex 2: output: 8
nums = [5, 2, 1, 2, 5, 2, 1, 2, 5]
print(sol.maximumUniqueSubarray(nums))

# ex 3: output: 30
nums = [5, 2, 1, 3, 4, 6, 9, 2, 5]
print(sol.maximumUniqueSubarray(nums))

# ex 4: output: 1
nums = [1, 1, 1]
print(sol.maximumUniqueSubarray(nums))

# ex 5: output: 100
nums = [99, 1, 99]
print(sol.maximumUniqueSubarray(nums))

# ex 6: output: 15
nums = [1, 2, 5, 2, 4, 1, 3, 5, 3, 6]
print(sol.maximumUniqueSubarray(nums))

# ex 7: output: 66
nums = [6, 7, 24, 2, 7, 22, 7, 5, 3, 2, 8, 9, 7, 22, 6, 4, 9, 3, 2, 1, 7, 4]
print(sol.maximumUniqueSubarray(nums))
