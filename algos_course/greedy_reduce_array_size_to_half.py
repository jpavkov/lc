"""
You are given an integer array arr. You can choose a set 
of integers and remove all the occurrences of these integers 
in the array.

Return the minimum size of the set so that at least half 
of the integers of the array are removed.

Example 1:
Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.

Example 2:
Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only possible set you can choose is {7}. This will make the new array empty.

Constraints:
    2 <= arr.length <= 105
    arr.length is even.
    1 <= arr[i] <= 105
"""

from collections import defaultdict
import heapq

class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        
        map_count = defaultdict(int)
        heap = []
        cur_size = len(arr)
        half_size = cur_size / 2
        removed_num = 0

        for i in arr:
            map_count[i] += 1

        for v in map_count.values():
            heapq.heappush(heap, -v)

        while cur_size > half_size:
            remove_value = -heapq.heappop(heap)
            cur_size -= remove_value
            removed_num += 1
        
        return removed_num

sol = Solution()

arr = [3,3,3,3,5,5,5,2,2,7]
print(sol.minSetSize(arr))

arr = [7,7,7,7,7,7]
print(sol.minSetSize(arr))

arr = [1,9]
print(sol.minSetSize(arr))
