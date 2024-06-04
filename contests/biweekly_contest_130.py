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
        limit = 1000000001
        dic = {}

        for index, char in enumerate(s):
            num = max(abs(points[index][0]), abs(points[index][1]))
            cur = dic.get(char, -1)
            if cur == -1:
                dic[char] = num
            else:
                dic[char] = min(num, cur)
                limit = min(limit, max(num, cur) - 1)
        
        for k, v in dic.items():
            print(k, v)
        
        print(f"limit {limit}")

        ans = 0
        for value in dic.values():
            if value <= limit:
                ans += 1
        
        return ans
        



## run tests
sol = Solution()

# problem 1
# grid = [[1,0,2],[1,0,2]]
# print(sol.satisfiesConditions(grid))
# grid = [[1,1,1],[0,0,0]]
# print(sol.satisfiesConditions(grid))
# grid = [[1],[2],[3]]
# print(sol.satisfiesConditions(grid))

# problem 2
points = [[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]]
s = "abdca"
print(sol.maxPointsInsideSquare(points, s))

points = [[1,1],[-2,-2],[-2,2]]
s = "abb"
print(sol.maxPointsInsideSquare(points, s))

points = [[1,1],[-1,-1],[2,-2]]
s = "ccd"
print(sol.maxPointsInsideSquare(points, s))

# problem 3


# problem 4



