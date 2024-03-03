from typing import List
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)+1):
                ans.append(len(set(nums[i:j]))**2)
        return sum(ans)
    
s = Solution()
a = s.sumCounts([1,2,1]) 
print(a)
