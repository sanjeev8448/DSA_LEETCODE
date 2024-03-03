from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums=sorted(nums)
        diff=float('inf')
        for i in range(len(nums)-1):
            start=i+1
            end=len(nums)-1
            while(start<end):
                sum=nums[i]+nums[start]+nums[end]
                if sum==target:
                    return target
                elif abs(target-sum)<diff:
                    diff=abs(target-sum)
                    ans=sum
                if sum>target:
                    end-=1
                else:
                    start+=1
        return ans
    
s = Solution()
a = s.threeSumClosest([-1,2,1,-4],1) 
print(a)
