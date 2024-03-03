from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] # pair [num:minLeft] , mono decreasing
        curMin = nums[0]
        # print(curMin)

        for n in nums[1:]:
            while stack and n >= stack[-1][0]:
                # print(stack)
                stack.pop()
                # print(stack)

            if stack and n > stack[-1][1]:
                return True
            
            stack.append([n,curMin])
            # print(stack)
            curMin = min(curMin,n)
        
        return False

s = Solution()
a = s.find132pattern([3,1,4,2])
print(a)