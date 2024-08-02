# https://leetcode.com/contest/biweekly-contest-135/
# https://leetcode.com/problems/find-the-winning-player-in-coin-game/description/
# https://leetcode.com/problems/minimum-length-of-string-after-operations/
# https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal/


class Solution:
    def losingPlayer(self, x: int, y: int) -> str:

        if min(x // 1, y // 4) % 2 == 0:
            return "Bob"

        return "Alice"

    def minimumLength(self, s: str) -> int:

        dic = {}
        ans = 0

        for c in s:
            dic[c] = dic.get(c, 0) + 1

        for v in dic.values():
            if v % 2 == 1:
                ans += 1
            else:
                ans += 2

        return ans

    def minChanges(self, nums: list[int], k: int) -> int:

        dic = {}
        ans = 0
        maxFit = 0
        inRange = 0
        outOfRange = 0

        for i in range(0, (len(nums) // 2)):
            diff = abs(nums[i] - nums[len(nums) - i - 1])
            dic[diff] = dic.get(diff, 0) + 1

        keyArray = dic.keys()
        filteredKeys = [key for key in keyArray if key <= k]

        for key in filteredKeys:
            diff = dic.get(key)
            maxFit = max(maxFit, diff)
            inRange += diff

        ##
        outOfRange = len(nums) - (inRange * 2)
        inRange = inRange - maxFit
        ans = outOfRange + inRange
        return ans


sol = Solution()

# # minChanges
# nums = [1, 0, 1, 2, 4, 3]
# k = 4
# print(sol.minChanges(nums, k))

nums = [0, 1, 2, 3, 3, 6, 5, 4]
k = 6
print(sol.minChanges(nums, k))

# # minimumLength
# s = "abaacbcbb"
# print(sol.minimumLength(s))

# s = "aa"
# print(sol.minimumLength(s))


# # losingPlayer
# x = 2
# y = 7
# print(sol.losingPlayer(x, y))

# x = 4
# y = 11
# print(sol.losingPlayer(x, y))
