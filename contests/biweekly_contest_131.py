# https://leetcode.com/contest/biweekly-contest-131/
# https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/description/
# https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/description/


class Solution:
    def duplicateNumbersXOR(self, nums: list[int]) -> int:
        seen = set()
        ans = 0

        for i in nums:
            if i in seen:
                ans ^= i
            else:
                seen.add(i)

        return ans

    def occurrencesOfElement(self, nums: list[int], queries: list[int], x: int) -> list[int]:
        numList = []
        ans = [-1] * len(queries)
        print(ans)
        for i, num in enumerate(nums):
            if num == x:
                numList.append(i)

        for i, num in enumerate(queries):
            if num <= len(numList):
                ans[i] = numList[num - 1]

        return ans


sol = Solution()
# occurences of element
nums = [1, 3, 1, 7]
queries = [1, 3, 2, 4]
x = 1
print(sol.occurrencesOfElement(nums, queries, x))

nums = [1, 2, 3]
queries = [10]
x = 5
print(sol.occurrencesOfElement(nums, queries, x))


# duplicate numbers
# nums = [1, 2, 1, 3]
# print(sol.duplicateNumbersXOR(nums))

# nums = [1, 2, 3]
# print(sol.duplicateNumbersXOR(nums))

# nums = [1, 2, 2, 1]
# print(sol.duplicateNumbersXOR(nums))
