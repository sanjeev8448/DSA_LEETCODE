from typing import List
import collections
from collections import deque
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = collections.defaultdict(list)
        blue = collections.defaultdict(list)

        for src,dst in redEdges:
            red[src].append(dst)
        # print(red)
        
        for src,dst in blueEdges:
            blue[src].append(dst)
        # print(blue)

        answer = [-1 for i in range(n)]
        q = deque()
        q.append([0,0,None]) # [node,length,prev_edge_color]
        visit = set()
        visit.add((0,None)) # (node,prev_edge_color)

        while q:
            node,length,edgecolor = q.popleft()
            if answer[node] == -1:
                answer[node] = length

            if edgecolor != "RED":
                for nei in red[node]:
                    if (nei,'RED') not in visit:
                        visit.add((nei,'RED'))
                        q.append([nei,length+1,'RED'])

            
            if edgecolor != "BLUE":
                for nei in blue[node]:
                    if (nei,'BLUE') not in visit:
                        visit.add((nei,'BLUE'))
                        q.append([nei,length+1,'BLUE'])
        return answer
    



s = Solution()
res = s.shortestAlternatingPaths(3,[[0,1],[1,2]],[])
print(res)