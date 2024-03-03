from typing import List
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        for i in range(len(arr) -1, -1, -1):      # [1,6,4,5,18,17]
            newMax = max(rightMax, arr[i])          
            # print(newMax)
            arr[i] = rightMax                 # [-1,-1,-1,-1,-1,-1]
            print(arr[i])
            # print(rightMax)
            rightMax = newMax                # [1,6,6,6,18,18]
            # print(rightMax)
        return arr


s = Solution()
a = s.replaceElements([17,18,5,4,6,1])
print(a)