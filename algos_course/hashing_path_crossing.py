"""
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', 
each representing moving one unit north, south, east, or 
\west, respectively. You start at the origin (0, 0) on a 
2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that 
is, if at any time you are on a location you have previously 
visited. Return false otherwise.

Example 1:
Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.

Example 2:
Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.

Constraints:
    1 <= path.length <= 104
    path[i] is either 'N', 'S', 'E', or 'W'.
"""


class Solution:
    def isPathCrossing(self, path: str) -> bool:

        point = set()
        x = 0
        y = 0
        point.add((x, y))

        for c in path:
            if c == "N":
                y += 1
            elif c == "S":
                y -= 1
            elif c == "E":
                x += 1
            else:
                x -= 1
            if (x, y) in point:
                return True
            point.add((x, y))

        return False


sol = Solution()

# ex 1: False
path = "NES"
print(sol.isPathCrossing(path))

# ex 2: True
path = "NESWW"
print(sol.isPathCrossing(path))
