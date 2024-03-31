"""
Given a string s, find the length of the longest substring without repeating characters. 

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

Strategy: use set, loop through str, filling up set and adding temp value. if char
already in set, reset temp value and assign ans to max(ans, temp value)
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        ans = 0
        left = -1

        for i, char in enumerate(s):
            if char in dic:
                left = max(left, dic[char])
            ans = max(ans, i - left)
            dic[char] = i

        return ans


sol = Solution()
print(sol.lengthOfLongestSubstring("abcdefg"))  # 7
print(sol.lengthOfLongestSubstring("abcabcd"))  # 4
print(sol.lengthOfLongestSubstring("aaaaaaa"))  # 1
print(sol.lengthOfLongestSubstring(""))  # 0
print(sol.lengthOfLongestSubstring(" %"))  # 2
print(sol.lengthOfLongestSubstring("dvdf"))  # 3
print(sol.lengthOfLongestSubstring("pwwkew"))  # 3
print(sol.lengthOfLongestSubstring("p"))  # 1
print(sol.lengthOfLongestSubstring("abba"))  # 2
