# https://leetcode.com/contest/weekly-contest-401/
# https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/description/
# https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/

class Solution:
    def numberOfChild(self, n: int, k: int) -> int:

        fromEnd = k % (n - 1)
        if (k // (n - 1)) % 2 == 0:
            return fromEnd

        return (n - 1) - fromEnd

    def valueAfterKSeconds(self, n: int, k: int) -> int:

        listN = [1] * n

        for _ in range(1, k + 1):
            for i in range(1, n):
                listN[i] = listN[i] + listN[i - 1]

        return listN[n - 1] % 1000000007


sol = Solution()

# valueAfterKSecond
n = 4
k = 5
print(sol.valueAfterKSeconds(n, k))

n = 5
k = 3
print(sol.valueAfterKSeconds(n, k))


# # numberOfChild
# n = 3
# k = 5
# print(sol.numberOfChild(n, k))
# n = 5
# k = 6
# print(sol.numberOfChild(n, k))
# n = 4
# k = 2
# print(sol.numberOfChild(n, k))
# n = 2
# k = 1
# print(sol.numberOfChild(n, k))
# n = 2
# k = 3
# print(sol.numberOfChild(n, k))
