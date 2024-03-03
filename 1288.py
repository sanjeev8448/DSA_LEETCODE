from typing import List
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:   
        intervals.sort(key=lambda i: (i[0],-i[1]))

        res = [intervals[0]]
        for l,r in intervals[1:]:
            prevL,prevR = res[-1]

            if prevL <= l and prevR >= r:
                continue
            res.append([l,r])
        return len(res)

s = Solution()
a = s.removeCoveredIntervals([[1,4],[3,6],[2,8]]) 
print(a)
