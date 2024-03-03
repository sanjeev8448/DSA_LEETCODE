from typing import List
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(a,b) for a,b in connections}
        # print(edges)
        neighbors = {city:[] for city in range(n)}
        # print(neighbors)
        visit = set()
        changes = 0

        for a,b in connections:
            neighbors[a].append(b)
            # print(neighbors)
            neighbors[b].append(a)
        # print(neighbors)

        def dfs(city):
            nonlocal edges,neighbors,visit,changes

            for neighbor in neighbors[city]:
                if neighbor in visit:
                    continue
                # check if neighbor can reach city 0
                if (neighbor,city) not in edges:
                    changes += 1
                visit.add(neighbor)
                dfs(neighbor)
        
        visit.add(0)
        dfs(0)
        return changes

s = Solution()
res = s.minReorder(6,[[0,1],[1,3],[2,3],[4,0],[4,5]])
print(res)