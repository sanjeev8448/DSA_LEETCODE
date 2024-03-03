from typing import List
from collections import defaultdict
# class Solution:
#     def minOperations(self, nums: List[int]) -> int:
#         res = 0
#         count = defaultdict(int)

#         for n in nums:
#             count[n] += 1

#         for n,c in count.items():
#             if c % 2 == 0:
#                 res += c // 2
#                 continue
#             elif c % 3 == 0:
#                 res += c // 3
#                 continue
#             else:
#                 return -1
#         return res
#         # print(count)
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        from collections import Counter
        mp = Counter(nums)
        
        count = 0
        for t in mp.values():
            if t == 1:
                return -1
            count += t // 3
            if t % 3:
                count += 1
                
        return count



s = Solution()
a = s.minOperations([2,3,3,2,2,4,2,3,4]) 

print(a)
            