# Using Moore’s Voting Algorithm
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count = {}
        # res,maxCount = 0,0
        # for n in nums:
        #     count[n] = 1 + count.get(n,0)
        #     # print(count)
        #     res = n if count[n] > maxCount else res
        #     print(res)
        #     maxCount = max(count[n],maxCount)
        # return res

        res,count = 0,0

        for n in nums:
            if count == 0:
                res = n
                # print(count)
                # print(res)
            count += (1 if n==res else -1)
            print(count)
        return res

s = Solution()
a = s.majorityElement([3,2,3])
print(a)