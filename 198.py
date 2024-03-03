from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1,rob2 = 0,0

        for n in nums:
            temp = max(n+rob1,rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
    
s = Solution()
a = s.rob([2,7,9,3,1])
print(a)

# linear time -> O(N) , space -> O(1)
        