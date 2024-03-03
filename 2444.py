from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        bad = min_ = max_ = -1
        res = 0

        for i,n in enumerate(nums):
            if not minK<=n<=maxK:
                bad = i

            if minK == n:
                min_ = i
            
            if maxK == n:
                max_ = i

            start = min(min_,max_)

            if start>bad:
                res += (start-bad)

        return res
        