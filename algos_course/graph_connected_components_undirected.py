"""
You have a graph of n nodes. You are given an integer 
n and an array edges where edges[i] = [ai, bi] indicates 
that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

Example 1:
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1

Constraints:
1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.
"""
from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        
        seen = set()
        graph = defaultdict(list)
        ans = 0

        # build graph as dictionary
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def traverseGraph(node):
            if node not in seen:
                seen.add(node)
            connections = graph.get(node)
            for i in connections:
                if i not in seen:
                    traverseGraph(i)

        # traverse dictionary starting w/ each key
        for k in graph.keys():
            if k not in seen:
                seen.add(k)
                ans += 1
                traverseGraph(k)

        unconnectedNodes = n - len(seen)
        return ans + unconnectedNodes


n = 5
edges = [[0,1],[1,2],[3,4]]
sol = Solution()
result = sol.countComponents(n, edges)
print(result)

n = 5
edges = [[0,1],[1,2],[2,3],[3,4]]
sol = Solution()
result = sol.countComponents(n, edges)
print(result)

n = 4
edges = [[2,3],[1,2],[1,3]]
sol = Solution()
result = sol.countComponents(n, edges)
print(result)