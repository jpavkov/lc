# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        nums.sort()

        for i, num in enumerate(nums):
            if k > 0 and num < 0:
                nums[i] = -num
                k -= 1

        if k % 2 == 1:
            return sum(nums) - (min(nums) * 2)
        return sum(nums)


sol = Solution()
nums = [4, 2, 3]
k = 1
print(sol.largestSumAfterKNegations(nums, k))

nums = [3, -1, 0, 2]
k = 3
print(sol.largestSumAfterKNegations(nums, k))

nums = [2, -3, -1, 5, -4]
k = 2
print(sol.largestSumAfterKNegations(nums, k))
