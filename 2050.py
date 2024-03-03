from typing import List
from collections import defaultdict
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = defaultdict(list)
        for src,dst in relations:
            adj[src].append(dst)

        max_time = {}  # src -> max_time
        def dfs(src):
            if src in max_time:
                return max_time[src]
            
            res = time[src-1]
            for nei in adj[src]:
                res = max(res,time[src-1] + dfs(nei))
            max_time[src]= res
            return res

        for i in range(1,n+1):
            dfs(i)
        
        return max(max_time.values())

s = Solution()
a = s.minimumTime(5,[[1,5],[2,5],[3,5],[3,4],[4,5]],[1,2,3,4,5]) 
print(a)