# https://leetcode.com/contest/weekly-contest-403/
# https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/
# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/description/


class Solution:
    def minimumAverage(self, nums: list[int]) -> float:

        ans = max(nums) + 1

        while len(nums) > 0:
            maxN = nums.pop(nums.index(max(nums)))
            minN = nums.pop(nums.index(min(nums)))
            ans = min(ans, (maxN + minN) / 2)

        return ans

    def minimumArea(self, grid: list[list[int]]) -> int:

        up, left = len(grid) + 1, len(grid[0]) + 1
        right, down = -1, -1

        for rowNum, row in enumerate(grid):
            if max(row) > 0:
                up = min(up, rowNum)
                down = max(down, rowNum)
                left = min(left, row.index(1))
                right = max(right, len(row) - 1 - row[::-1].index(1))

        print(f"up: {up}, left: {left}, down: {down}, right: {right}")
        return ((down + 1 - up) * (right + 1 - left))


sol = Solution()
# minimumArea
grid = [[0, 1, 0], [1, 0, 1]]
print(sol.minimumArea(grid))

grid = [[1, 0], [0, 0]]
print(sol.minimumArea(grid))


# minimumAverage
# nums = [7, 8, 3, 4, 15, 13, 4, 1]
# print(sol.minimumAverage(nums))

# nums = [1, 9, 8, 3, 10, 5]
# print(sol.minimumAverage(nums))

# nums = [1, 2, 3, 7, 8, 9]
# print(sol.minimumAverage(nums))
