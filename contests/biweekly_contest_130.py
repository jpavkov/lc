"""
https://leetcode.com/problems/check-if-grid-satisfies-conditions/
https://leetcode.com/problems/maximum-points-inside-the-square/
https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/
https://leetcode.com/problems/find-products-of-elements-of-big-array/
"""

class Solution:
    def satisfiesConditions(self, grid: list[list[int]]) -> bool:
        ans = True

        m = len(grid)
        n = len(grid[0])

        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if i < m - 1:
                    if grid[i][j] != grid[i + 1][j]:
                        return False
                if j < n - 1:
                    if grid[i][j] == grid[i][j + 1]:
                        return False

        return ans

    def maxPointsInsideSquare(self, points: list[list[int]], s: str) -> int:
        max = 1000000001
        dic = {}

        for index, char in s:
            num = max(abs(points[index][0], points[index][1]))
            dic[char] = max(num, dic.get(char, -1))
        



## run tests
sol = Solution()

# problem 1
grid = [[1,0,2],[1,0,2]]
print(sol.satisfiesConditions(grid))
grid = [[1,1,1],[0,0,0]]
print(sol.satisfiesConditions(grid))
grid = [[1],[2],[3]]
print(sol.satisfiesConditions(grid))

# problem 2


# problem 3


# problem 4



