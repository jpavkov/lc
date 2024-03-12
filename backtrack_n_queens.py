"""
The n-queens puzzle is the problem of placing n queens 
on an n x n chessboard such that no two queens attack 
each other.

Given an integer n, return the number of distinct 
solutions to the n-queens puzzle.

Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:
Input: n = 1
Output: 1

Constraints: 1 <= n <= 9
"""

class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def addNotValid(i):
            # add row
            for j in (i * n, (i * n) + n - 1):
                notValid.add(j)
            
            # add columns
            for j in (i, n * n, n):
                notValid.add(j)

            # add diagonals
            for j in (i, n * n, n + 1):
                notValid.add(j)

            # add anti-diagonals
            for j in (i, n * n, n - 1):
                anti = i
                while anti >= 0:
                    notValid.add(j)
                    

        def backtrack(curr, qCount):
            if qCount == n:
                ans += 1

            for i in range(0, n - 1):
                curr.append(i)
                qCount += 1
                addNotValid(i)


        notValid = set()
        ans = 0
        backtrack([], 0)
        return ans


sol = Solution()
for i in range(1, 9):
    ans = sol.totalNQueens(i)
    print(f"number of solutions for a {i}x{i} board: {ans}")

