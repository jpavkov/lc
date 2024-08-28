# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/description/

class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()
        i = 0
        j = 0

        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                i += 1
            j += 1

        return i


sol = Solution()
players = [4, 7, 9]
trainers = [8, 2, 5, 8]
print(sol.matchPlayersAndTrainers(players, trainers))

players = [1, 1, 1]
trainers = [10]
print(sol.matchPlayersAndTrainers(players, trainers))
