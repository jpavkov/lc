"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s 
can be replaced to get t.

All occurrences of a character must be replaced with another 
character while preserving the order of characters. No two 
characters may map to the same character, but a character may 
map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Constraints:
    1 <= s.length <= 5 * 104
    t.length == s.length
    s and t consist of any valid ascii character.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        sDic = {}
        tDic = {}

        for index, char in enumerate(s):
            if char in sDic:
                sDic[char] += index
            else:
                sDic[char] = index

        for index, char in enumerate(t):
            if char in tDic:
                tDic[char] += index
            else:
                tDic[char] = index

        for i in range(len(s)):
            if sDic[s[i]] != tDic[t[i]]:
                return False

        return True


sol = Solution()

# ex 1: output: True
s = "egg"
t = "add"
print(sol.isIsomorphic(s, t))

# ex 2: output: False
s = "foo"
t = "bar"
print(sol.isIsomorphic(s, t))

# ex 3: output: True
s = "paper"
t = "title"
print(sol.isIsomorphic(s, t))
