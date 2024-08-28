# https://leetcode.com/problems/earliest-possible-day-of-full-bloom/description/

class Solution:
    def earliestFullBloom(self, plantTime: list[int], growTime: list[int]) -> int:
        combined = [[p, g + 1] for p, g in zip(plantTime, growTime)]
        combined.sort(key=lambda x: (-x[1], -x[0]))
        print(combined)

        plantDays = 0
        totalDays = 0

        for time in combined:
            plantDays += time[0]
            totalDays = max(totalDays, plantDays + time[1])

        return totalDays - 1


sol = Solution()
plantTime = [1, 4, 3]
growTime = [2, 3, 1]
print(sol.earliestFullBloom(plantTime, growTime))

plantTime = [1, 2, 3, 2]
growTime = [2, 1, 2, 1]
print(sol.earliestFullBloom(plantTime, growTime))

plantTime = [1]
growTime = [1]
print(sol.earliestFullBloom(plantTime, growTime))
