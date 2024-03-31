"""
Given an array of integers arr, return true if the number of 
occurrences of each value in the array is unique or false 
otherwise.

Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. 
    No two values have the same number of occurrences.

Example 2:
Input: arr = [1,2]
Output: false

Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

Constraints:
    1 <= arr.length <= 1000
    -1000 <= arr[i] <= 1000
"""


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:

        dic = {}

        for num in arr:
            dic[num] = dic.get(num, 0) + 1

        unique = set(dic.values())

        return len(unique) == len(dic.values())


sol = Solution()

# ex 1: Output: True
arr = [1, 2, 2, 1, 1, 3]
print(sol.uniqueOccurrences(arr))

# ex 2: Output: False
arr = [1, 2]
print(sol.uniqueOccurrences(arr))

# ex 3: Output: True
arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
print(sol.uniqueOccurrences(arr))
