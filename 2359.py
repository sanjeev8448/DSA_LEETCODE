from typing import List
import collections
from collections import defaultdict,deque
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        adj = collections.defaultdict(list)
        for i,dst in enumerate(edges):
            adj[i].append(dst)
        # print(adj)

        def bfs(src,distMap):
            q = deque()
            q.append([src,0])
            distMap[src] = 0

            while q:
                node,dist = q.popleft()
                for nei in adj[node]:
                    if nei not in distMap:
                        q.append([nei,dist+1])
                        distMap[nei] = dist+1
        
        node1Dist = {} # map node -> distance from node1
        node2Dist = {} # map node -> distance from node2

        bfs(node1,node1Dist)
        bfs(node2,node2Dist)

        res = -1
        resDist = float('inf')
        for i in range(len(edges)):
            if i in node1Dist and i in node2Dist:
                dist = max(node1Dist[i],node2Dist[i])
                if dist < resDist:
                    res = i
                    resDist = dist
        return res


s = Solution()
res = s.closestMeetingNode([2,2,3,-1],0,1)
print(res)
