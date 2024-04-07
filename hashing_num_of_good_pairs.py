"""
1512. Number of Good Pairs
Easy
Topics: Array, Hash Table, Math, Counting

Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Example 1:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:
Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Example 3:
Input: nums = [1,2,3]
Output: 0

Constraints:
    1 <= nums.length <= 100
    1 <= nums[i] <= 100
"""


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:

        dic = {}
        ans = 0

        for num in nums:
            dic[num] = dic.get(num, 0) + 1
            ans += (dic[num] - 1)

        return ans


sol = Solution()


# ex 1: output: 4
nums = [1, 2, 3, 1, 1, 3]
print(sol.numIdenticalPairs(nums))

# ex 2: output: 6
nums = [1, 1, 1, 1]
print(sol.numIdenticalPairs(nums))

# ex 3: output: 0
nums = [1, 2, 3]
print(sol.numIdenticalPairs(nums))
