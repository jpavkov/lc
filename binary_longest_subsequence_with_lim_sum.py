"""
You are given an integer array nums of length n, 
and an integer array queries of length m.

Return an array answer of length m where answer[i] 
is the maximum size of a subsequence that you can 
take from nums such that the sum of its elements is 
less than or equal to queries[i].

A subsequence is an array that can be derived from 
another array by deleting some or no elements without 
changing the order of the remaining elements.

Example 1:
Input: nums = [4,5,2,1], queries = [3,10,21]
Output: [2,3,4]
Explanation: We answer the queries as follows:
- The subsequence [2,1] has a sum less than or equal to 3. 
    It can be proven that 2 is the maximum size of such a 
    subsequence, so answer[0] = 2.
- The subsequence [4,5,1] has a sum less than or equal to 10. 
    It can be proven that 3 is the maximum size of such a 
    subsequence, so answer[1] = 3.
- The subsequence [4,5,2,1] has a sum less than or equal to 21. 
    It can be proven that 4 is the maximum size of such a 
    subsequence, so answer[2] = 4.

Example 2:
Input: nums = [2,3,4,5], queries = [1]
Output: [0]
Explanation: The empty subsequence is the only subsequence that has a sum less than or equal to 1, so answer[0] = 0.
 

Constraints:

n == nums.length
m == queries.length
1 <= n, m <= 1000
1 <= nums[i], queries[i] <= 10^6
"""
import heapq

class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:

        n = len(nums)
        nums_min_sum = [0] * (n + 1)
        m = len(queries)
        ans = [-1] * m

        heapq.heapify(nums)

        for i in range(1, n + 1):
            nums_min_sum[i] = nums_min_sum[i - 1] + heapq.heappop(nums)

        print(nums_min_sum)

        for index, val in enumerate(queries):
            left = 1
            right = n

            if val < nums_min_sum[left]:
                ans[index] = 0
            elif val >= nums_min_sum[right]:
                ans[index] = right
            else:
                while right - left > 1:
                    midline = left + ((right - left) // 2)
                    if nums_min_sum[midline] >= val:
                        right = midline
                    else:
                        left = midline

                if val == nums_min_sum[right]:
                    ans[index] = right
                else:
                    ans[index] = left

        return ans

sol = Solution()

nums = [4,5,2,1]
queries = [3,10,21]
print(sol.answerQueries(nums, queries))

nums = [2,3,4,5]
queries = [1]
print(sol.answerQueries(nums, queries))

nums = [736411,184882,914641,37925,214915]
queries = [331244,273144,118983,118252,305688,718089,665450]
print(sol.answerQueries(nums, queries))