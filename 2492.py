from typing import List
import collections
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = collections.defaultdict(list)  # node -> list of (neighbor,dist)
        for src,dst,dist in roads:
            adj[src].append((dst,dist))
            adj[dst].append((src,dist))
        # print(adj)

        def dfs(i):
            if i in visit:
                return
            visit.add(i)
            nonlocal res
            for nei,dist in adj[i]:
                res = min(res,dist)
                dfs(nei)
        
        res = float('inf')
        visit = set()
        dfs(1)
        return res
            

s = Solution()
res = s.minScore(4,[[1,2,9],[2,3,6],[2,4,5],[1,4,7]])
print(res)