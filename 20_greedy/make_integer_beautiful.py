# https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/description/

class Solution():
    def makeIntegerBeautiful(self, n: int, target: int) -> int:

        base_ten = 10
        n_roundup = n

        while sum(int(integer) for integer in str(n_roundup)) > target:
            n_roundup += base_ten - (n_roundup % base_ten)
            base_ten *= 10

        return n_roundup - n


sol = Solution()

# makeIntegerBeautiful
n = 16
target = 6
print(sol.makeIntegerBeautiful(n, target))

n = 467
target = 6
print(sol.makeIntegerBeautiful(n, target))

n = 1
target = 1
print(sol.makeIntegerBeautiful(n, target))