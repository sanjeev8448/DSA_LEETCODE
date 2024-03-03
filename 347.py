from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # using-Bucket sort()
        count = {}    # {1: 3, 2: 2, 3: 1}
        freq = [[] for i in range(len(nums)+1)]  # [[], [], [], [], [], [], []]
        # print(freq)

        for n in nums:
            count[n] = 1 + count.get(n,0)
            # print(count)

        for n,c in count.items():
            # print(n)  # 1,2,3 - key
            # print(c)    # 3,2,1 - value
            freq[c].append(n)
            # print(freq)  # [[], [3], [2], [1], [], [], []]

        res = []
        for i in range(len(freq)-1,0,-1):  # 6,5,4,3,2
            # print(len(freq))
            # print(i)
            # print(i)
            for n in freq[i]:
                # print(n)
                res.append(n)
                if len(res) == k:
                    return res

s = Solution()
a = s.topKFrequent([1,1,1,2,2,3],2)
print(a)