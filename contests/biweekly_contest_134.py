# https://leetcode.com/contest/biweekly-contest-134/problems/alternating-groups-i/
# https://leetcode.com/problems/maximum-points-after-enemy-battles/description/
# https://leetcode.com/problems/alternating-groups-ii/description/

import heapq


class Solution():
    def numberOfAlternatingGroups(self, colors: list[int]) -> int:
        ans = 0

        listLength = len(colors)

        if (colors[0] == colors[listLength - 2] and colors[0] != colors[listLength - 1]):
            ans += 1

        if (colors[1] == colors[listLength - 1] and colors[1] != colors[0]):
            ans += 1

        for x in range(2, listLength):
            if (colors[x] == colors[x - 2] and colors[x] != colors[x - 1]):
                ans += 1

        return ans

    def maximumPoints(self, enemyEnergies: list[int], currentEnergy: int) -> int:

        points = 0
        minEnemy = min(enemyEnergies)

        # to get first point(s)
        points += int(currentEnergy / minEnemy)
        currentEnergy = currentEnergy % minEnemy

        # to extract largest enemy and get subsequent points
        if points >= 1:
            enemyEnergies = [-i for i in enemyEnergies]
            heapq.heapify(enemyEnergies)
            while len(enemyEnergies) > 1:
                currentEnergy += heapq.heappop(enemyEnergies) * -1
                points += int(currentEnergy / minEnemy)
                currentEnergy = currentEnergy % minEnemy

        return points

    def numberOfAlternatingGroups_two(self, colors: list[int], k: int) -> int:
        print(colors)
        colors += colors[:k - 1]
        print(colors)
        res = 0
        cnt = 1

        for i in range(1, len(colors)):
            if colors[i] != colors[i - 1]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= k:
                res += 1
        return res


sol = Solution()

# alternating groups 2
colors = [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0]
k = 12
# print(colors)
sol.numberOfAlternatingGroups_two(colors, k)

# colors = [0]
# sol.numberOfAlternatingGroups_two(colors, k)

colors = [0, 0]
print(colors)
sol.numberOfAlternatingGroups_two(colors, k)

colors = [1, 1, 1]
print(colors)
sol.numberOfAlternatingGroups_two(colors, k)

colors = [1, 0, 0]
print(colors)
sol.numberOfAlternatingGroups_two(colors, k)

colors = [1, 0, 1]
print(colors)
sol.numberOfAlternatingGroups_two(colors, k)


# alternating groups 1
# colors = [1, 1, 1]
# print(sol.numberOfAlternatingGroups(colors))

# colors = [0, 1, 0, 0, 1]
# print(sol.numberOfAlternatingGroups(colors))

# colors = [0, 1, 1]
# print(sol.numberOfAlternatingGroups(colors))

# enemy energies
# enemyEnergies = [3, 2, 2]
# currentEnergy = 2
# print(sol.maximumPoints(enemyEnergies, currentEnergy))

# enemyEnergies = [2]
# currentEnergy = 10
# print(sol.maximumPoints(enemyEnergies, currentEnergy))

# enemyEnergies = [2, 5]
# currentEnergy = 3
# print(sol.maximumPoints(enemyEnergies, currentEnergy))
