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


def lengthOfLongestSubstring(s: str) -> int:
    dic_char = {}
    local_ans = 0
    ans = 0

    for i, char in enumerate(s):
        if char in dic_char:
            # print(dic_char["w"])
            local_ans = i - dic_char[char]
        else:
            ans += 1
        dic_char[char] = i
        # print("i:", i)
        # print("ans:", ans)
        # print("char:", char)
        # print("dic_char[char]:", dic_char[char])

    return ans


# print(lengthOfLongestSubstring("abcdefg"))  # 7
# print(lengthOfLongestSubstring("abcabcd"))  # 4
# print(lengthOfLongestSubstring("aaaaaaa"))  # 1
# print(lengthOfLongestSubstring(""))  # 0
# print(lengthOfLongestSubstring(" %"))  # 2
# print(lengthOfLongestSubstring("dvdf"))  # 3
print(lengthOfLongestSubstring("pwwkew"))  # 3
