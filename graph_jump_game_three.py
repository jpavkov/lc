"""
Given an array of non-negative integers "arr", you are 
initially positioned at "start" index of the array. 
When you are at index "i", you can jump to "i + arr[i]" 
or "i - arr[i]", check if you can reach any index with 
value 0.

Notice that you can not jump outside of the array at any time.

Example 1:
Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
- All possible ways to reach at index 3 with value 0 are: 
    - index 5 -> index 4 -> index 1 -> index 3 
    - index 5 -> index 6 -> index 4 -> index 1 -> index 3 

Example 2:
Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true 
Explanation: 
- One possible way to reach at index 3 with value 0 is: 
    - index 0 -> index 4 -> index 1 -> index 3

Example 3:
Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0. 

Constraints:
    1 <= arr.length <= 5 * 104
    0 <= arr[i] < arr.length
    0 <= start < arr.length
"""

from collections import defaultdict, deque

class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        
        graph = defaultdict(list)
        queue = deque([start])
        seen = set()

        # build graph
        while queue:
            #branches = queue.popleft()
            #parent = branches[0]
            #children = branches[1]
            node = queue.popleft()
            distance = arr[node]
            if node not in seen:
                seen.add(node)
                if node + distance < len(arr):
                    graph[node].append(node + distance)
                    queue.append(node + distance)
                if node - distance >= 0:
                    graph[node].append(node - distance)
                    queue.append(node - distance)

        for k, v in graph.items():
            print(f"{k} - {v}")

        for i in enumerate(seen):
            print(i)
        #return True if 0 in seen else False





sol = Solution()

arr = [4,2,3,0,3,1,2]
start = 5
print(sol.canReach(arr, start))

arr = [4,2,3,0,3,1,2]
start = 0
print(sol.canReach(arr, start))

arr = [3,0,2,1,2]
start = 2
print(sol.canReach(arr, start))