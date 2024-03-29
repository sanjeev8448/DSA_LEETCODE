from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in numset:
                length = 0
                while (n+length) in numset:
                    length+=1
                longest = max(length,longest)

        return longest

s = Solution()
a = s.longestConsecutive([100,4,200,1,3,2])
print(a)