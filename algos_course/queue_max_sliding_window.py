"""
Given an integer array nums and an integer k, there is a sliding 
window of size k that moves from the very left to the very right. 
For each window, find the maximum element in the window.

Example:
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
return [3, 3, 5, 5, 6, 7]
"""

from collections import deque

def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    ans = []
    queue = deque()
    for i, num in enumerate(nums):
        # seeing if queue is not empty and current num > 
        while queue and num > nums[queue[-1]]:
            queue.pop()

        queue.append(i)

        if queue[0] + k == i:
            queue.popleft()

        if i >= k - 1:
            ans.append(nums[queue[0]])

    return ans
            








test = [1, 3, 4, -1, -5, 0, 2, 6]
exp_ans = [4, 4, 4, 0, 2, 6]

print(maxSlidingWindow(test, 3))

test = [1, 3, -1, -3, 5, 3, 6, 7]
exp_ans = [3, 3, 5, 5, 6, 7]
