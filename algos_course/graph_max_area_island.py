"""
You are given an m x n binary matrix grid. An island 
is a group of 1's (representing land) connected 
4-directionally (horizontal or vertical.) You may 
assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a 
value 1 in the island.

Return the maximum area of an island in grid. If there 
is no island, return 0.

Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:

        seen = set()

        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0 or (i, j) in seen:
                return 0
            #grid[i][j] = 0 # turn square to 0 so already viewed
            seen.add((i, j))
            area = 1
            area += dfs(grid, i+1, j)
            area += dfs(grid, i-1, j)
            area += dfs(grid, i, j+1)
            area += dfs(grid, i, j-1)
            return area
        
        maxArea = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    maxArea = max(maxArea, dfs(grid, i, j))
        
        return maxArea

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

sol = Solution()
print(sol.maxAreaOfIsland(grid))

# print(grid[0][2])
# print(len(grid))
# print(len(grid[0]))