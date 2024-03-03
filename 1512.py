from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        result = 0
        
        for num in nums:
            if num in count:
                result += count[num]
                count[num] += 1
            else:
                count[num] = 1
        
        return result
    
s = Solution()
a = s.numIdenticalPairs([1,2,3,1,1,3]) 
print(a)