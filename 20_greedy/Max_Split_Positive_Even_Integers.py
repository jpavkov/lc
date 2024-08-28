# https://leetcode.com/problems/maximum-split-of-positive-even-integers/description/

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> list[int]:
        ans = []
        if finalSum % 2 == 1:
            return ans

        newNum = 2

        while finalSum >= newNum:
            ans.append(newNum)
            finalSum -= newNum
            newNum += 2

        print(f"newNum: {newNum}")
        print(f"finalSum: {finalSum}")

        if finalSum > 0:
            ans[-1] = ans[-1] + finalSum

        return ans


sol = Solution()
finalSum = 12
print(sol.maximumEvenSplit(finalSum))

finalSum = 7
print(sol.maximumEvenSplit(finalSum))

finalSum = 28
print(sol.maximumEvenSplit(finalSum))
