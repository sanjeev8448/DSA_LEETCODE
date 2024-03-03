from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):                       # t.c = O(n^2)
                if nums[i]+nums[j] == target:
                    ans.append(i)
                    ans.append(j)
        return ans

# another approach

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i in range(len(nums)):
            goal = target-nums[i]
            print(goal)
            if goal in ans:                        # t.c = O(n)
                return[ans[goal],i]
                print(goal)
            ans[nums[i]] = i
            print(ans)

s = Solution()
a = s.twoSum([2,7,11,15],9)
print(a)
        
 
