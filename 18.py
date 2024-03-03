from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()   #[-2,-1,0,0,1,2]   len = 6
        res, quad = [],[]

        def ksum(k,start,target):     # 4,0,target
            if k!=2:
                for i in range(start,len(nums)-k+1):         # 3 times run loop
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    quad.append(nums[i])
                    # print(quad)
                    ksum(k-1,i+1,target-nums[i])
                    # print(ksum)
                    quad.pop()
                    # print(quad)
                return
            
            # base case , Two sum II

            l,r = start , len(nums)-1

            while l < r :
                if nums[l] + nums[r] < target:
                    l+=1
                elif nums[l] + nums[r] > target:
                    r-=1
                else:
                    res.append(quad+[nums[l],nums[r]])
                    l+=1

                    while l < r and nums[l] == nums[l-1]:
                        l+=1

        ksum(4,0,target)
        return res
    
s = Solution()
x = s.fourSum([1,0,-1,0,-2,2],0)
print(x)

print(1<1)