# https://leetcode.com/problems/assign-cookies/description/

class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        j = 0

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
            j += 1

        return i


sol = Solution()
g = [1, 2, 3]
s = [1, 1]
print(sol.findContentChildren(g, s))

g = [1, 2]
s = [1, 2, 3]
print(sol.findContentChildren(g, s))
