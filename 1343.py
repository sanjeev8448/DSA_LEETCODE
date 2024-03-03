from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        curSum = sum(arr[:k-1])
        # print(curSum)

        for l in range(len(arr)-k+1):
            # print(len(arr)-k+1)
            curSum += arr[l+k-1]
            print(curSum)
            if (curSum/k) >= threshold:
                res += 1
            curSum -= arr[l]
        return res

s = Solution()
x = s.numOfSubarrays([2,2,2,2,5,5,5,8],3,4)
print(x)