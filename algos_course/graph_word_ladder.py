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
        
        # length of word used
        L = len(beginWord)

        # test if beginWord in wordList, if not add
        if beginWord not in wordList:
            wordList.append(beginWord)

        # test if endWord in wordList, if not return 0, if so return index
        if endWord in wordList:
            end_index = wordList.index(endWord)
        else:
            return 0

        # create graph of intermediate states
        graph = defaultdict(list)
        for word in wordList:
            for i in range(L):
                graph[word[:i] + "*" + word[i+1:]].append(word)

        # bfs of graph
        q = deque([(beginWord, 1)])
        seen = set()
        seen.add(beginWord)
        while q:
            cur_word, level = q.popleft()
            for i in range(L):
                intermediate_word = cur_word[:i] + "*" + cur_word[i+1:]
                for word in graph[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in seen:
                        seen.add(word)
                        q.append((word, level + 1))

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