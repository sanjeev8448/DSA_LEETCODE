from typing import List

class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int ) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, p in flights:  # s=source, d=dest, p=price
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]


s = Solution()
a = s.findCheapestPrice(4,[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],0,3,1)
print(a)