"""
A gene string can be represented by an 8-character long 
string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene 
string startGene to a gene string endGene where one mutation 
is defined as one single character changed in the gene string.
- For example, "AACCGGTT" --> "AACCGGTA" is one mutation.

There is also a gene bank "bank" that records all the valid gene 
mutations. A gene must be in "bank" to make it a valid gene string.

Given the two gene strings "startGene" and "endGene" and the gene 
bank "bank", return the minimum number of mutations needed to 
mutate from "startGene" to "endGene". If there is no such a mutation, 
return -1.

Note that the starting point is assumed to be valid, so it might 
not be included in the bank.

Example 1:
Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1

Example 2:
Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2

Constraints:
- 0 <= bank.length <= 10
- startGene.length == endGene.length == bank[i].length == 8
- startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
"""

from collections import defaultdict, deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        
        if endGene not in bank:
            return -1

        graph = defaultdict(list)
        seen = set()
        q = deque([(startGene, 0)])

        # ensure startGene and endGene in bank
        if startGene not in bank:
            bank.append(startGene)

        # create mutations as a helper function to show num of mutations between two genes
        def mutations(geneOne: str, geneTwo: str) -> int:
            return sum(char1 != char2 for char1, char2 in zip(geneOne, geneTwo))

        # create dictionary of key values
        for i in range(len(bank)):
            for j in range(i + 1, len(bank)):
                if mutations(bank[i], bank[j]) == 1:
                    graph[bank[i]].append(bank[j])
                    graph[bank[j]].append(bank[i])

        # traverse tree starting with startGene, and if you hit endGene, return levels
        while q:
            result = q.popleft()
            gene = result[0]
            level = int(result[1]) + 1
            singleMutes = graph.get(gene)
            for s in singleMutes:
                if s not in seen:
                    q.append([s, level])
                    seen.add(s)
                    if s == endGene:
                        return level
        
        return -1
        
startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
sol = Solution()
print(sol.minMutation(startGene, endGene, bank))

startGene = "AACCGGTT"
endGene = "AACCGGTA"
bank = ["AACCGGTA"]
sol = Solution()
print(sol.minMutation(startGene, endGene, bank))

startGene = "AACCGGTT"
endGene = "AACCGGTA"
bank = []
sol = Solution()
print(sol.minMutation(startGene, endGene, bank))