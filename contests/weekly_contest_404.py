# https://leetcode.com/contest/weekly-contest-404/
# https://leetcode.com/problems/maximum-height-of-a-triangle/description/
# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/description/


class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:

        def getHeight(r, b):
            rows = 1
            while True:
                if r < rows:
                    break
                r -= rows
                rows += 1
                if b < rows:
                    break
                b -= rows
                rows += 1
            return rows - 1

        return max(getHeight(red, blue), getHeight(blue, red))

    def maximumLength(self, nums: list[int]) -> int:

        odd, even, alternate = 0, 0, 0
        curr = nums[0] % 2

        for _, num in enumerate(nums):
            curr_mod = num % 2
            if curr_mod == 0:
                even += 1
            else:
                odd += 1
            if curr_mod != curr:
                curr = 1 - curr
                alternate += 1

        return max(odd, even, alternate + 1)


sol = Solution()
# maximum length
nums = [1, 2, 3, 4]
print(sol.maximumLength(nums))

nums = [1, 2, 1, 1, 2, 1, 2]
print(sol.maximumLength(nums))

nums = [1, 3]
print(sol.maximumLength(nums))

nums = [1, 3, 3, 2, 2, 4, 4, 5, 4, 5, 4, 4, 5, 5]
print(sol.maximumLength(nums))

nums = [1, 5, 9, 4, 2]
print(sol.maximumLength(nums))

nums = [1, 2, 5, 4, 9]
print(sol.maximumLength(nums))


# max height of triangle
# red = 2
# blue = 4
# print(sol.maxHeightOfTriangle(red, blue))

# red = 2
# blue = 1
# print(sol.maxHeightOfTriangle(red, blue))

# red = 1
# blue = 1
# print(sol.maxHeightOfTriangle(red, blue))

# red = 10
# blue = 1
# print(sol.maxHeightOfTriangle(red, blue))
