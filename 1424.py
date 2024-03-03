from typing import List
from collections import deque

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []

        q = deque([(0,0)])

        while q:
            row,col = q.popleft()
            res.append(nums[row][col])

            if col == 0 and row + 1 < len(nums):
                q.append((row+1,0))
            
            if col + 1 < len(nums[row]):
                q.append((row,col+1))
        
        return res
    

s = Solution()
a = s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])
print(a)