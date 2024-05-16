"""
Given a string s and an integer k, return the maximum 
number of vowel letters in any substring of s with 
length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

Constraints:
    1 <= s.length <= 105
    s consists of lowercase English letters.
    1 <= k <= s.length
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = set(['a', 'e', 'i', 'o', 'u'])
        left = right = count = 0
        sList = list(s)
        ans = 0

        for char in sList:
            if char in vowels:
                count += 1
                ans = max(ans, count)
            right += 1
            if right - left >= k:
                if sList[left] in vowels:
                    count -= 1
                left += 1

        return ans


sol = Solution()

# Example 1: Output: 3
s = "abciiidef"
k = 3
print(sol.maxVowels(s, k))

# Example 2: Output: 2
s = "aeiou"
k = 2
print(sol.maxVowels(s, k))

# Example 3: Output: 2
s = "leetcode"
k = 3
print(sol.maxVowels(s, k))

# Example 4: Output: 1
s = "a"
k = 1
print(sol.maxVowels(s, k))

# Example 5: Output: 0
s = "x"
k = 1
print(sol.maxVowels(s, k))
