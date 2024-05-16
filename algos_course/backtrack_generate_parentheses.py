"""
Given n pairs of parentheses, write a function to 
generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
    1 <= n <= 8
"""

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        def backtrack(open, close, curr_str):
            if len(curr_str) == n * 2:
                ans.append(curr_str)
                return
            
            if open > 0:
                curr_str = curr_str + "("
                backtrack(open - 1, close, curr_str)
                curr_str = curr_str[:-1]
            if open < close:
                curr_str = curr_str + ")"
                backtrack(open, close - 1, curr_str)
                curr_str = curr_str[:-1]

        ans = []
        backtrack(n, n, "")
        return ans




sol = Solution()
for i in range(5):
    print(sol.generateParenthesis(i))

