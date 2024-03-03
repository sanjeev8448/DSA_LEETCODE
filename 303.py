from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        cur = 0
        for n in nums:
            cur+=n
            self.prefix.append(cur)
        # print(self.prefix)
        

    def sumRange(self, left: int, right: int) -> int:
        rightsum = self.prefix[right]
        leftsum = self.prefix[left-1] if left>0 else 0
        return rightsum-leftsum

s = NumArray([-2, 0, 3, -5, 2, -1])
a = s.sumRange(2,5)                    #-3
print(a)