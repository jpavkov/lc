# https://leetcode.com/contest/weekly-contest-400/
# https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/description/
# https://leetcode.com/problems/count-days-without-meetings/description/
# https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/


class Solution:
    def minimumChairs(self, s: str) -> int:
        ans = 0
        cur = 0
        for c in s:
            if c == "E":
                cur += 1
                ans = max(ans, cur)
            else:
                cur -= 1
        return ans

    def countDays(self, days: int, meetings: list[list[int]]) -> int:

        meetings.sort()
        ans = 0
        start = meetings[0][0]
        stop = meetings[0][1]

        for m in meetings[1:]:
            if m[0] <= stop + 1:
                stop = max(stop, m[1])
            else:
                ans += stop - start + 1
                start = m[0]
                stop = m[1]

        ans += stop - start + 1

        return days - ans

    def clearStars(self, s: str) -> str:
        char_to_indices = {i: [] for i in range(26)}
        removed_indices = set()

        for index, char in enumerate(s):
            if char == '*':
                for i in range(0, 26):
                    if len(char_to_indices[i]) > 0:
                        removed_indices.add(char_to_indices[i].pop())
                        break
            else:
                char_to_indices[ord(char) - 97].append(index)

        ans = ''
        for i, c in enumerate(s):
            if not (c == '*' or i in removed_indices):
                ans += c

        return ans


sol = Solution()

# clearStars
s = "aaba*"
print(sol.clearStars(s))
s = "abc"
print(sol.clearStars(s))

# # countDays
# days = 10
# meetings = [[5, 7], [1, 3], [9, 10]]
# print(sol.countDays(days, meetings))  # 2
# days = 5
# meetings = [[2, 4], [1, 3]]
# print(sol.countDays(days, meetings))  # 1
# days = 6
# meetings = [[1, 6]]
# print(sol.countDays(days, meetings))  # 0

# # minimumChairs
# s = "EEEEEEE"
# print(sol.minimumChairs(s))
# s = "ELELEEL"
# print(sol.minimumChairs(s))
# s = "ELEELEELLL"
# print(sol.minimumChairs(s))
