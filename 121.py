from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        maxProfit = 0
        minPurchase = prices[0]
        # print(minPurchase)
        for i in range(1, len(prices)):		
            # print(prices[i])12
            maxProfit = max(maxProfit, prices[i] - minPurchase)
            minPurchase = min(minPurchase, prices[i])
            print(minPurchase)
        return maxProfit

s = Solution()
a = s.maxProfit([7,1,5,3,6,4])
print(a)