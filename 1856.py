from typing import List
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        res = 0
        stack = []
        prefix = [0]
        for n in nums:
            prefix.append(prefix[-1]+n)
        
        for i,n in enumerate(nums):
            newStart = i
            while stack and stack[-1][1] > n:
                start,val = stack.pop()
                total = prefix[i] - prefix[start]
                res = max(res,val*total)
                newStart = start
            stack.append((newStart,n))

        for start,val in stack:
            total = prefix[len(nums)] - prefix[start]
            res = max(res,val*total)
        
        return res % (10**9 + 7)

s = Solution()
a = s.maxSumMinProduct([1,2,3,2]) 
print(a)
# [3,1,5,6,4,2]