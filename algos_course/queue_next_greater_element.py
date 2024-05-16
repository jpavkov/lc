"""
The next greater element of some element x in an array is the 
first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, 
where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that 
nums1[i] == nums2[j] and determine the next greater element 
of nums2[j] in nums2. If there is no next greater element, 
then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] 
is the next greater element as described above.

 

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
 
Constraints:
1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.
"""

def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    # implement a stack in descending order for nums2
    # implement a map for nums2
    # reference key of map for values in nums 1 and return value from corresponding key

    stack = []
    ans = []
    dic = {}

    for i, val in enumerate(nums2):
        if i == 0 or val < stack[-1]:
            stack.append(val)
        else:
            # pop and assign to dictionary
            while stack and stack[-1] < val:
                dic[stack.pop()] = val
            stack.append(val)

    for i, val in enumerate(nums1):
        ans.append(dic.get(val, -1))
    
    return ans
        



nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1, nums2))

nums1 = [2,4]
nums2 = [1,2,3,4]
print(nextGreaterElement(nums1, nums2))

nums1 = [1,3,4,5,10]
nums2 = [4,1,2,3,7,6,5,10,8,9]
print(nextGreaterElement(nums1, nums2))

