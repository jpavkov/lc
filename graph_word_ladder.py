"""
A transformation sequence from word "beginWord" to word 
"endWord" using a dictionary "wordList" is a sequence of 
words "beginWord -> s1 -> s2 -> ... -> sk" such that:
    Every adjacent pair of words differs by a single letter.
    Every "si" for "1 <= i <= k" is in "wordList". Note that 
        "beginWord" does not need to be in wordList.
    "sk == endWord"

Given two words, "beginWord" and "endWord", and a dictionary 
"wordList", return the number of words in the shortest 
transformation sequence from "beginWord" to "endWord", or "0"
if no such sequence exists.

 

Example 1:
Input: 
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation:
    One shortest transformation sequence is 
    "hit" -> "hot" -> "dot" -> "dog" -> cog", 
    which is 5 words long.

Example 2:
Input:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: 
    The endWord "cog" is not in wordList, 
    therefore there is no valid transformation 
    sequence.
 

Constraints:
    1 <= beginWord.length <= 10
    endWord.length == beginWord.length
    1 <= wordList.length <= 5000
    wordList[i].length == beginWord.length
    beginWord, endWord, and wordList[i] consist of lowercase English letters.
    beginWord != endWord
    All the words in wordList are unique.
"""

from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        
        # test if beginWord in wordList, if not add. return index
        if beginWord not in wordList:
            wordList.append(beginWord)
        begin_index = wordList.index(beginWord)

        # test if endWord in wordList, if not return 0, if so return index
        if endWord in wordList:
            end_index = wordList.index(endWord)
        else:
            return 0

        # create helper function to see if two words are 1 letter apart
        def sequenceMatch(word1, word2) -> int:
            return sum(char1 != char2 for char1, char2 in zip(word1, word2))

        # create index based map using defaultdict
        graph = defaultdict(list)
        for i, x in enumerate(wordList):
            for j, y in enumerate(wordList[i + 1:], start = i + 1):
                if sequenceMatch(x, y) == 1:
                    graph[i].append(j)
                    graph[j].append(i)

        for k, v in graph.items():
            print(f"{k} - {v}")


        all_combo_dict = defaultdict(list)
        L = len(beginWord)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

        for k, v in all_combo_dict.items():
            print(f"{k} - {v}")

        # # perform BFS on map. start with beginWord. use list(index, level) in queue
        # seen = set()
        # q = deque([(begin_index, 1)])
        # while q:
        #     node, level = q.popleft()
        #     if node not in seen:
        #         seen.add(node)
        #         values = graph.get(node)
        #         if values:
        #             level += 1
        #             for v in values:
        #                 if v == end_index:
        #                     return level
        #                 q.append([v, level])

        return 0

sol = Solution()

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(sol.ladderLength(beginWord, endWord, wordList))

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
print(sol.ladderLength(beginWord, endWord, wordList))