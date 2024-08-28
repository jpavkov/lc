# https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/description/

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:

        ans = ['a'] * n
        k -= n

        while k > 0:
            n -= 1
            remains = min(k, 25)
            ans[n] = chr(ord('a') + remains)
            k -= remains

        return ''.join(ans)

        # This is a great solution!!!
        # z = (k - n) // 25
        # c = (k - n) % 25
        # a = n - z

        # if c:
        #     return 'a' * (a - 1) + chr(97 + c) + 'z' * z

        # return 'a' * a + 'z' * z


sol = Solution()
n = 3
k = 27
print(sol.getSmallestString(n, k))

n = 5
k = 73
print(sol.getSmallestString(n, k))

n = 5
k = 130
print(sol.getSmallestString(n, k))

n = 12
k = 207
print(sol.getSmallestString(n, k))
