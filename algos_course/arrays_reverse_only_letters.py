"""
Given a string s, reverse the string according 
to the following rules:
    All the characters that are not English 
        letters remain in the same position.
    All the English letters (lowercase or 
        uppercase) should be reversed.

Return s after reversing it.

Example 1:
Input: s = "ab-cd"
Output: "dc-ba"

Example 2:
Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:
Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

Constraints:
    1 <= s.length <= 100
    s consists of characters with ASCII values in the range [33, 122].
    s does not contain '\"' or '\\'.
"""


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        if len(s) == 1:
            return s

        sList = list(s)
        ans = [0] * len(s)

        left = 0
        right = len(sList) - 1

        while left <= right:

            while not sList[left].isalpha() and left < right:
                ans[left] = sList[left]
                left += 1

            while not sList[right].isalpha() and right > left:
                ans[right] = sList[right]
                right -= 1

            if left == right:
                ans[left] = sList[left]
                left += 1
            else:
                ans[left] = sList[right]
                ans[right] = sList[left]
                left += 1
                right -= 1

        return "".join(ans)


sol = Solution()

# ex 1
s = "ab-cd"
print(sol.reverseOnlyLetters(s))

# ex 2
s = "a-bC-dEf-ghIj"
print(sol.reverseOnlyLetters(s))

# ex 3
s = "Test1ng-Leet=code-Q!"
print(sol.reverseOnlyLetters(s))
