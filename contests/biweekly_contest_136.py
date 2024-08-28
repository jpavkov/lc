# https: // leetcode.com/contest/biweekly-contest-136/
# https: // leetcode.com/problems/find-the-number-of-winning-players/description/
# https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/description/
# https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-ii/description/


class Solution:
    def winningPlayerCount(self, n: int, pick: list[list[int]]) -> int:

        ans = 0
        my_dict = {}

        for p in pick:
            if p[0] not in my_dict:
                my_dict[p[0]] = [0] * 11

            my_dict[p[0]][p[1]] += 1

        for k, v in my_dict.items():
            # print(f"k: {k}, v: {v}")
            if k < max(v):
                ans += 1

        return ans

    def minFlips(self, grid: list[list[int]]) -> int:
        rowCount = len(grid)
        colCount = len(grid[0])

        rowChanges = 0
        colChanges = 0

        for i in range(rowCount):
            for j in range(colCount // 2):
                if grid[i][j] != grid[i][colCount - j - 1]:
                    rowChanges += 1

        for i in range(colCount):
            for j in range(rowCount // 2):
                if grid[j][i] != grid[rowCount - j - 1][i]:
                    colChanges += 1

        return min(rowChanges, colChanges)


sol = Solution()
grid = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
print(sol.minFlips(grid))

grid = [[0, 1], [0, 1], [0, 0]]
print(sol.minFlips(grid))

grid = [[1], [0]]
print(sol.minFlips(grid))

# n = 4
# pick = [[0, 0], [1, 0], [1, 0], [2, 1], [2, 1], [2, 0]]
# print(sol.winningPlayerCount(n, pick))

# n = 5
# pick = [[1, 1], [1, 2], [1, 3], [1, 4]]
# print(sol.winningPlayerCount(n, pick))

# n = 5
# pick = [[1, 1], [2, 4], [2, 4], [2, 4]]
# print(sol.winningPlayerCount(n, pick))
