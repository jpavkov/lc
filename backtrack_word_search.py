"""
Given an m x n grid of characters board and a string 
word, return true if word exists in the grid.

The word can be constructed from letters of sequentially 
adjacent cells, where adjacent cells are horizontally or 
vertically neighboring. The same letter cell may not be 
used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.
"""


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])
        curr_word = 0

        def backtrack(row, col, seen, index):
            if len(word) == index + 1:
                return True
            
            if (row, col) not in seen and word[index] == board[row][col]:
                seen.add([(row, col)])
                backtrack

        backtrack(([0, 0]), set(), 0)

        return False
    



sol = Solution()

# Example 1, Output: true
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"


# Example 2, Output: true
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"


# Example 3, Output: false
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"



