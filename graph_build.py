from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> defaultdict:

        # build a graph
        n = len(isConnected)
        print("n",n)
        graph = defaultdict(list)
        for i in range(n):
            print("row",i, isConnected[i])
            for j in range(i + 1, n):
                print("j",j)
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
        
        return graph
    
sol = Solution()
graph = sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
for k,v in graph.items():
    print(f"{k} - {v}")

graph = sol.findCircleNum([[1,0,0],[0,1,0],[0,0,1]])
for k,v in graph.items():
    print(f"{k} - {v}")