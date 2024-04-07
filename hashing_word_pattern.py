"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection 
between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Constraints:
    1 <= pattern.length <= 300
    pattern contains only lower-case English letters.
    1 <= s.length <= 3000
    s contains only lowercase English letters and spaces ' '.
    s does not contain any leading or trailing spaces.
    All the words in s are separated by a single space.
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patternDic = {}
        sDic = {}

        for index, char in enumerate(pattern):
            if char not in patternDic:
                patternDic[char] = index

        words = s.split()

        for index, word in enumerate(words):
            if word not in sDic:
                sDic[word] = index

        if len(pattern) == len(words):
            for i in range(len(words)):
                if patternDic[pattern[i]] != sDic[words[i]]:
                    return False
        else:
            return False
        return True


sol = Solution()

# Example 1: Output: true
pattern = "abba"
s = "dog cat cat dog"
print(sol.wordPattern(pattern, s))

# Example 2: Output: false
pattern = "abba"
s = "dog cat cat fish"
print(sol.wordPattern(pattern, s))

# Example 3: Output: false
pattern = "aaaa"
s = "dog cat cat dog"
print(sol.wordPattern(pattern, s))
