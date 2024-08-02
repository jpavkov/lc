# https://leetcode.com/contest/biweekly-contest-133/
# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/description/
# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/description/

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        counter = 0
        for i in nums:
            if i % 3 != 0:
                counter += 1
        return counter

    def minOperations(self, nums: list[int]) -> int:

        counter = 0

        for i in range(0, len(nums) - 2):
            if nums[i] == 0:
                nums[i] = 1
                counter += 1
                nums[i + 1] = 1 - nums[i + 1]
                nums[i + 2] = 1 - nums[i + 2]

        if sum(nums[-2:]) == 2:
            return counter

        return -1

    def minOperations_two(self, nums: list[int]) -> int:
        counter = 0

        if nums[0] == 0:
            counter += 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                counter += 1

        return counter


sol = Solution()
# minOperations_two
nums = [0, 1, 1, 0, 1]
print(sol.minOperations_two(nums))

nums = [1, 0, 0, 0]
print(sol.minOperations_two(nums))


# minOperations
# nums = [0, 1, 1, 1, 0, 0]
# print(sol.minOperations(nums))

# nums = [0, 1, 1, 1]
# print(sol.minOperations(nums))

# minimumOperations
# nums = [1, 2, 3, 4]
# print(sol.minimumOperations(nums))

# nums = [3, 6, 9]
# print(sol.minimumOperations(nums))
