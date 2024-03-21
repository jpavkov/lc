"""
Given two strings text1 and text2, return the length of 
their longest common subsequence. If there is no common 
subsequence, return 0.

A subsequence of a string is a new string generated from 
the original string with some characters (can be none) 
deleted without changing the relative order of the remaining 
characters.
    For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is 
common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:
    1 <= text1.length, text2.length <= 1000
    text1 and text2 consist of only lowercase English characters.
"""
from functools import cache
class Solution:
    def longestCommonSubsequenceCache(self, text1: str, text2: str) -> int:
        @cache
        def dp(i, j):
            if len(text1) == i or len(text2) == j:
                return 0

            if text1[i] == text2[j]:
                return 1 + dp(i + 1, j + 1)

            return max(dp(i + 1, j), dp(i, j + 1))

        return dp(0, 0)

    def longestCommonSubsequenceMemo(self, text1: str, text2: str) -> int:

        def dp(i, j):
            if len(text1) == i or len(text2) == j:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + dp(i + 1, j + 1)
            else:
                memo[(i, j)] = max(dp(i + 1, j), dp(i, j + 1))

            return memo[(i, j)]

        memo = {}
        return dp(0, 0)

    def longestCommonSubsequenceBottomUp(self, text1: str, text2: str) -> int:

        n = len(text1)
        m = len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

                # print(f"for i: {i}, j: {j}")
                # for row in enumerate(dp):
                #     print(row[1])

        return dp[n][m]

sol = Solution()

text1 = "abcde"
text2 = "ace"
cache_ans = sol.longestCommonSubsequenceCache(text1, text2)
memo_ans = sol.longestCommonSubsequenceMemo(text1, text2)
bottom_ans = sol.longestCommonSubsequenceBottomUp(text1, text2)
print(f"text 1: {text1}")
print(f"text 2: {text2}")
print(f"cache: {cache_ans}")
print(f"memo: {memo_ans}")
print(f"bottom: {bottom_ans}")
print("\n")

text1 = "abc"
text2 = "abc"
cache_ans = sol.longestCommonSubsequenceCache(text1, text2)
memo_ans = sol.longestCommonSubsequenceMemo(text1, text2)
bottom_ans = sol.longestCommonSubsequenceBottomUp(text1, text2)
print(f"text 1: {text1}")
print(f"text 2: {text2}")
print(f"cache: {cache_ans}")
print(f"memo: {memo_ans}")
print(f"bottom: {bottom_ans}")
print("\n")


text1 = "abc"
text2 = "def"
cache_ans = sol.longestCommonSubsequenceCache(text1, text2)
memo_ans = sol.longestCommonSubsequenceMemo(text1, text2)
bottom_ans = sol.longestCommonSubsequenceBottomUp(text1, text2)
print(f"text 1: {text1}")
print(f"text 2: {text2}")
print(f"cache: {cache_ans}")
print(f"memo: {memo_ans}")
print(f"bottom: {bottom_ans}")
print("\n")

