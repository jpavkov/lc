"""
You're given strings jewels representing the types of stones 
that are jewels, and stones representing the stones you have. 
Each character in stones is a type of stone you have. 
You want to know how many of the stones you have are also jewels. 
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0
 
Constraints:
1 <= jewels.length, stones.length <= 50
jewels and stones consist of only English letters.
All the characters of jewels are unique.

Strategy: craete a map of stones, the iterate through jewels and add up values in stones
"""


def numJewelsInStones(jewels: str, stones: str) -> int:
    ans = 0
    dic_stones = {}

    for char in stones:
        dic_stones[char] = dic_stones.get(char, 0) + 1

    for char in jewels:
        ans += dic_stones.get(char, 0)

    return ans


print(numJewelsInStones("aA", "AAA"))  # 3
print(numJewelsInStones("aA", "a"))  # 1
print(numJewelsInStones("aA", "bcbc"))  # 0
print(numJewelsInStones("aA", "aAaA"))  # 4
