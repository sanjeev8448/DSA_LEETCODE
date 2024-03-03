from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_can = max(candies)
        res = []

        for i in range(len(candies)):
            if candies[i]+extraCandies >= max_can:
                res.append(True)
            else:
                res.append(False)

        return res
           

s = Solution()
a = s.kidsWithCandies([2,3,5,1,3],3)
print(a)