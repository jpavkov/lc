# Given two strings ransomNote and magazine, return true if
# ransomNote can be constructed by using the letters from magazine
# and false otherwise. Each letter in magazine can only be used once in ransomNote.

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

# strategy: create a dictionary with the note and magazine, where each letter is the key,
# and value is the times it shows up. Then iterate over dictionary and compare values
# to the magazine. ans = True to start, and returns as false once magazine values <
# note values


def canConstruct(ransomNote: str, magazine: str) -> bool:
    ans = True
    dic_r = {}
    dic_m = {}

    for char in ransomNote:
        dic_r[char] = dic_r.get(char, 0) + 1

    for char in magazine:
        dic_m[char] = dic_m.get(char, 0) + 1

    for key in dic_r:
        if dic_r.get(key) > dic_m.get(key, 0):
            return False

    return ans


print(canConstruct("aa", "a"))
print(canConstruct("ab", "ab"))
print(canConstruct("", "ab"))
print(canConstruct("ab", ""))
print(canConstruct("a", "aa"))
