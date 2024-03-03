import heapq
from typing import List
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:


        heap = []
        for h in range(len(heights)-1):
            diff = heights[h+1] - heights[h]
            if diff <= 0:
                continue

            bricks -= diff
            heapq.heappush(heap,-diff)

            if bricks < 0:
                if ladders == 0:
                    return h
                ladders -= 1
                bricks += -heapq.heappop(heap)
        return len(heights) - 1
          
 
s = Solution()
res = s.furthestBuilding([4,12,2,7,3,18,20,3,19],10,2)
print(res)
