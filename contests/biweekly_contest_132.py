# https://leetcode.com/contest/biweekly-contest-132/
# https://leetcode.com/problems/clear-digits/description/
# https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row/description/
# https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/description/


class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for char in s:
            if char.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        return "".join(stack)

    def findWinningPlayer(self, skills: list[int], k: int) -> int:

        counter = 0
        location = 0
        maxNum = skills[0]

        for i in range(1, len(skills)):
            if skills[i] > maxNum:
                counter = 1
                location = i
                maxNum = skills[i]
            else:
                counter += 1

            if counter == k:
                return location

        return location

    def maximumLength(self, nums: list[int], k: int) -> int:
        return 0


sol = Solution()
# s = "abc"
# print(sol.clearDigits(s))

# s = "cb34"
# print(sol.clearDigits(s))


skills = [4, 2, 6, 3, 9]
k = 2
print(sol.findWinningPlayer(skills, k))

skills = [2, 5, 4]
k = 3
print(sol.findWinningPlayer(skills, k))
