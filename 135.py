from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = [1] * len(ratings)

        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                res[i] += 1

        for i in range(len(ratings)-2,-1,-1):
            if res[i] > ratings[i+1]:
                res[i] += 1
        return sum(res)

s = Solution()
a = s.candy([1,2,1,2] )
print(a)
