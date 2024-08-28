# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        # s = list(s)
        # t = list(t)
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1

        return len(t) - j


sol = Solution()
s = "coaching"
t = "coding"
print(sol.appendCharacters(s, t))

s = "abcde"
t = "a"
print(sol.appendCharacters(s, t))

s = "z"
t = "abcde"
print(sol.appendCharacters(s, t))
