from typing import List
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = {} # hashmap -> TRUE/FALSE
        n = len(graph)
        
        def dfs(i):
            if i in safe:
                return safe[i]
            
            safe[i] = False
            for nei in graph[i]:
                if not dfs(nei):
                    return safe[i]
                
            safe[i] = True
            return safe[i]

        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res



s = Solution()
a = s.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]])
print(a)