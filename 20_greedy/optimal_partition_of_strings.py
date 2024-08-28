# https://leetcode.com/problems/optimal-partition-of-string/description/

class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        ans = 1

        for c in s:
            if c in seen:
                seen.clear()
                ans += 1
            seen.add(c)

        return ans


sol = Solution()
s = "abacaba"
print(sol.partitionString(s))

s = "ssssss"
print(sol.partitionString(s))
