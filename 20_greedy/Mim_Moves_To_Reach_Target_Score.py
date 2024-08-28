# https://leetcode.com/problems/minimum-moves-to-reach-target-score/description/
# https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/description/

class Solution():
    def minMoves(self, target: int, maxDoubles: int) -> int:

        count = 0

        while target > 1:
            if target % 2 == 1:
                target -= 1
                count += 1
            else:
                if maxDoubles > 0:
                    target /= 2
                    count += 1
                    maxDoubles -= 1
                else:
                    count += target - 1
                    break
                    # target -= target

        return int(count)

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


# minMoves
# target = 5
# maxDoubles = 0
# print(sol.minMoves(target, maxDoubles))

# target = 19
# maxDoubles = 2
# print(sol.minMoves(target, maxDoubles))

# target = 10
# maxDoubles = 4
# print(sol.minMoves(target, maxDoubles))
