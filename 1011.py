from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights),sum(weights)
        # print(l)
        # print(r)        
        res = r
        def canShip(cap):
            ships,currCap = 1,cap
            for w in weights:
                if currCap - w < 0:
                    # print(w)
                    # print(currCap)
                    ships += 1
                    currCap = cap
                currCap -= w
                print(currCap)

            return ships <= days
        
        while l <= r:
            cap = (l+r)//2
            # print(cap)
            if canShip(cap):
                res = min(res,cap)
                r = cap - 1
            else:
                l = cap + 1
        return res
s = Solution()
a = s.shipWithinDays([1,2,3,4,5,6,7,8,9,10],5)
print(a)