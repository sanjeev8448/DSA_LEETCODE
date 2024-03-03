from typing import List
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        # print(piles)
        res = 0

        for i in range(len(piles) // 3, len(piles), 2):
            # print(i)
            res += piles[i]
        
        return res
S = Solution()
a = S.maxCoins([2,4,1,2,7,8])
print(a)