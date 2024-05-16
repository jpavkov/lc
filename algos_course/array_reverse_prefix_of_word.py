"""
Given a 0-indexed string word and a character ch, reverse the 
segment of word that starts at index 0 and ends at the index 
of the first occurrence of ch (inclusive). If the character 
ch does not exist in word, do nothing.
    - For example, if word = "abcdefd" and ch = "d", then you 
    should reverse the segment that starts at 0 and ends at 3 
    (inclusive). The resulting string will be "dcbaefd".

Return the resulting string.

Example 1:
Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"
Explanation: The first occurrence of "d" is at index 3. 
    - Reverse the part of word from 0 to 3 (inclusive), 
    the resulting string is "dcbaefd".

Example 2:
Input: word = "xyxzxe", ch = "z"
Output: "zxyxxe"
Explanation: The first and only occurrence of "z" is at index 3.
    - Reverse the part of word from 0 to 3 (inclusive), 
    the resulting string is "zxyxxe".

Example 3:
Input: word = "abcd", ch = "z"
Output: "abcd"
Explanation: "z" does not exist in word.
    - You should not do any reverse operation, the resulting 
    string is "abcd".

Constraints:
    1 <= word.length <= 250
    word consists of lowercase English letters.
    ch is a lowercase English letter.
"""


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        word_array = list(word)

        right = 0
        match = False

        while right < len(word_array) and not match:
            if str(word_array[right]) == ch:
                match = True
                left = 0
                while left < right:
                    left_char = word_array[left]
                    word_array[left] = word_array[right]
                    word_array[right] = left_char
                    left += 1
                    right -= 1
            right += 1

        return "".join(word_array)


sol = Solution()

# ex 1, output: "dcbaefd"
word = "abcdefd"
ch = "d"
print(sol.reversePrefix(word, ch))

# ex 2, output: "zxyxxe"
word = "xyxzxe"
ch = "z"
print(sol.reversePrefix(word, ch))

# ex 3, output: "abcd"
word = "abcd"
ch = "z"
print(sol.reversePrefix(word, ch))
