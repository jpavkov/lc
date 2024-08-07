"""
Given a string s, sort it in decreasing order based on the 
frequency of the characters. The frequency of a character 
is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, 
return any of them.

Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear 
    once. So 'e' must appear before both 'r' and 't'. 
    Therefore "eetr" is also a valid answer.

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both 
    "cccaaa" and "aaaccc" are valid answers. Note that "cacaca" 
    is incorrect, as the same characters must be together.

Example 3:
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is 
    incorrect. Note that 'A' and 'a' are treated as two 
    different characters.

Constraints:
    1 <= s.length <= 5 * 105
    s consists of uppercase and lowercase English letters and digits.
"""


class Solution:
    def frequencySort(self, s: str) -> str:

        dic = {}
        fre = []
        ans = ""

        for char in s:
            dic[char] = dic.get(char, 0) + 1

        for v in dic.values():
            if v not in fre:
                fre.append(v)

        fre.sort(reverse=True)

        for num in fre:
            for k, v in dic.items():
                if v == (num):
                    ans = ans + "".join([k] * v)

        return ans


sol = Solution()

# ex 1: Output: "eert"
s = "tree"
print(sol.frequencySort(s))

# ex 2: Output: "aaaccc"
s = "cccaaa"
print(sol.frequencySort(s))

# ex 3: Output: "bbAa"
s = "Aabb"
print(sol.frequencySort(s))

s = "abaccadeeefaafcc"
print(sol.frequencySort(s))
