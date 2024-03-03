from typing import List
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        CountGap = {0:0} # mapping pos: count of bricks gap

        for r in wall:
            total = 0
            for b in r[:-1]:
                total += b
                CountGap[total] = 1 + CountGap.get(total,0)


        return len(wall) - max(CountGap.values())

s = Solution()
a = s.leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]])
print(a)