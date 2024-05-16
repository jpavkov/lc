# https://leetcode.com/contest/weekly-contest-397/problems/permutation-difference-between-two-strings/
# https://leetcode.com/contest/weekly-contest-397/problems/taking-maximum-energy-from-the-mystic-dungeon/

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ans = 0
        sDic = {}
                
        # create a dictionary for s
        for index, char in enumerate(s):
            sDic[char] = index

        # iterate through t and compare to s
        for index, char in enumerate(t):
            ans += abs(index - sDic[char])

        return ans
    
    def maximumEnergy(self, energy: list[int], k: int) -> int:
        ans = -1001
        
        for i in range(1, k + 1):
            curr_ans = energy[len(energy) - i]
            temp = curr_ans
            for j in range(len(energy) - i - k, -1, -k):
                curr_ans += energy[j]
                temp = max(temp, curr_ans)
            ans = max(ans, temp)
        
        return ans


sol = Solution()
s = "abc"
t = "bac"
print(sol.findPermutationDifference(s,t))

s = "abcde"
t = "edbac"
print(sol.findPermutationDifference(s,t))

energy = [5,2,-10,-5,1]
k = 3
print(sol.maximumEnergy(energy, k))

energy = [-2,-3,-1]
k = 2
print(sol.maximumEnergy(energy, k))

energy = [8, -5]
k = 1
print(sol.maximumEnergy(energy, k))
