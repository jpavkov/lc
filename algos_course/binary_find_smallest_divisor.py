"""
Given an array of integers nums and an integer threshold, 
we will choose a positive integer divisor, divide all the 
array by it, and sum the division's result. Find the smallest 
divisor such that the result mentioned above is less than or 
equal to threshold.

Each result of the division is rounded to the nearest integer 
greater than or equal to that element. (For example: 7/3 = 3 
and 10/2 = 5).

The test cases are generated so that there will be an answer.

Example 1:
Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: 
    We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
    If the divisor is 4 we can get a sum of 7 (1+1+2+3).
    If the divisor is 5 the sum will be 5 (1+1+1+2). 

Example 2:
Input: nums = [44,22,33,11,1], threshold = 5
Output: 44

Constraints:
    1 <= nums.length <= 5 * 104
    1 <= nums[i] <= 106
    nums.length <= threshold <= 106
"""
import math
class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        
        left = 0
        right = max(nums)

        while right - left > 1:
            mid = math.ceil((left + right) / 2)
            result = sum(map(lambda x : math.ceil(x / mid), nums))
            if result > threshold:
                left = mid
            else:
                right = mid

        if sum(map(lambda x : math.ceil(x / right), nums)) <= threshold:
            return right
        return left

sol = Solution()

# first input
nums = [1,2,5,9]
threshold = 6
print(sol.smallestDivisor(nums,threshold))

# second input
nums = [44,22,33,11,1]
threshold = 5
print(sol.smallestDivisor(nums,threshold))

nums = [2,3,5,7,11]
threshold = 11
print(sol.smallestDivisor(nums,threshold))