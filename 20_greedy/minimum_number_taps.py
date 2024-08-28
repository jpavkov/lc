# https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/description/

class Solution:
    def minTaps(self, n: int, ranges: list[int]) -> int:
        intervals = [0] * (n + 1)
        for i, r in enumerate(ranges):
            if i + r > intervals[i]:
                left = max(0, i - r)
                right = min(n, i + r) + 1
                intervals[left:right] = [ranges[i] + i] * (right - left)

        if intervals[0] == 0:
            return -1
        if intervals[0] == n:
            return 1

        i = 0
        count = 0

        while i < intervals[i] and intervals[i] < n:
            i = intervals[i]
            count += 1

        if intervals[i] < n:
            return -1

        return count + 1


sol = Solution()

n = 5
ranges = [3, 4, 1, 1, 0, 0]
print(sol.minTaps(n, ranges))

n = 3
ranges = [0, 0, 0, 0]
print(sol.minTaps(n, ranges))

n = 7
ranges = [1, 2, 1, 0, 2, 1, 0, 1]
print(sol.minTaps(n, ranges))
