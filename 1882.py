from typing import List
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg = 0
        for n in nums:
            if n == 0:
                return 0
            neg += (1 if n < 0 else 0)
        # print(neg)
        # print(neg%2)
        
        return -1 if neg % 2 else 1
    
s = Solution()
# a = s.arraySign([-1,-2,-3,-4,3,2,1])
# a = s.arraySign([1,5,0,2,-3])
a = s.arraySign([-1,1,-1,1,-1])
print(a)