"""
1657. Determine if Two Strings Are Close

Two strings are considered close if you can attain one from 
the other using the following operations:
    Operation 1: Swap any two existing characters.
        For example, abcde -> aecdb
    Operation 2: Transform every occurrence of one existing 
    character into another existing character, and do the 
    same with the other character.
        For example, aacabb -> bbcbaa (all a's turn into b's, 
        and all b's turn into a's)

You can use the operations on either string as many times as 
necessary.

Given two strings, word1 and word2, return true if word1 and 
word2 are close, and false otherwise.

Example 1:
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
    Apply Operation 1: "abc" -> "acb"
    Apply Operation 1: "acb" -> "bca"

Example 2:
Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or 
    vice versa, in any number of operations.

Example 3:
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
    Apply Operation 1: "cabbba" -> "caabbb"
    Apply Operation 2: "caabbb" -> "baaccc"
    Apply Operation 2: "baaccc" -> "abbccc"

Constraints:
    1 <= word1.length, word2.length <= 105
    word1 and word2 contain only lowercase English letters.
"""


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1) != len(word2):
            return False

        dic1 = {}
        dic2 = {}

        for c in word1:
            dic1[c] = dic1.get(c, 0) + 1

        for c in word2:
            if c not in dic1:
                return False
            dic2[c] = dic2.get(c, 0) + 1

        if len(dic1) != len(dic2):
            return False

        values_list1 = list(dic1.values())
        values_list2 = list(dic2.values())

        values_list1.sort()
        values_list2.sort()

        if values_list1 != values_list2:
            return False

        return True


sol = Solution()

# ex 1: output: true
word1 = "abc"
word2 = "bca"
print(sol.closeStrings(word1, word2))

# ex 2: output: false
word1 = "a"
word2 = "aa"
print(sol.closeStrings(word1, word2))

# ex 3: output: true
word1 = "cabbba"
word2 = "abbccc"
print(sol.closeStrings(word1, word2))

# ex 4: output: false
word1 = "aua"
word2 = "ssx"
print(sol.closeStrings(word1, word2))
