# https://leetcode.com/problems/longest-palindrome/description/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict = {}
        longest_negative_used = False
        for c in s:
            dict[c] = dict.get(c, 0) + 1

        ans = 0
        vals = sorted(dict.values(), reverse=True)
        for num in vals:
            if num % 2 == 0:
                ans += num
            elif not longest_negative_used:
                ans += num
                longest_negative_used = True
            else:
                ans += num - 1

        # return ans


sol = Solution()
s = "abccccdd"
print(sol.longestPalindrome(s))

s = "a"
print(sol.longestPalindrome(s))
