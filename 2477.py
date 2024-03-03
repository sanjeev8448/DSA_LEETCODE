import collections
import math as m
from typing import List
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj = collections.defaultdict(list)
        for src,dst in roads:
            adj[src].append(dst)
            adj[dst].append(src)
        # print(adj)

        def dfs(node,parent):
            nonlocal res
            passengers = 0
            for child in adj[node]:
                if child != parent:
                    p = dfs(child,node)
                    passengers += p
                    res += int(m.ceil(p/seats))
            return passengers + 1
        
        res = 0
        dfs(0,-1)
        return res


s = Solution()
res = s.minimumFuelCost([[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]],2)
print(res)