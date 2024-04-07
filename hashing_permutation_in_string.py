"""
567. Permutation in String
Medium
Topics: Hash Table, Two Pointers, String, Sliding Window

Given two strings s1 and s2, return true if s2 contains 
a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations 
is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
    1 <= s1.length, s2.length <= 104
    s1 and s2 consist of lowercase English letters.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        dic1 = {}

        for c in s1:
            dic1[c] = dic1.get(c, 0) + 1

        list2 = list(s2)

        for left, c in enumerate(list2):
            if c in dic1 and len(list2) - left >= len(s1):
                # build dic2 and compare
                dic2 = {}
                for i in range(left, left + len(s1)):
                    if list2[i] in dic1:
                        dic2[list2[i]] = dic2.get(list2[i], 0) + 1
                    else:
                        break
                if len(dic1) == len(dic2):
                    ans = True
                    for k, v in dic1.items():
                        if v != dic2.get(k, 0):
                            ans = False
                    if ans:
                        return True

        return False


sol = Solution()

# Example 1: Output: True
s1 = "ab"
s2 = "eidbaooo"
print(sol.checkInclusion(s1, s2))

# Example 2: Output: False
s1 = "ab"
s2 = "eidboaoo"
print(sol.checkInclusion(s1, s2))
