# https://leetcode.com/problems/container-with-most-water/description/

class Solution():
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0

        while left < right:
            area = max(area, (right - left) * min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return area


sol = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(sol.maxArea(height))

height = [1, 1]
print(sol.maxArea(height))

height = [2, 3, 4, 5, 18, 17, 6]
print(sol.maxArea(height))
