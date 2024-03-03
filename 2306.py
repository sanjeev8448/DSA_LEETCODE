from typing import List
import collections
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # map first char -> list of word suffixes
        wordMap = collections.defaultdict(set)
        for w in ideas:
            wordMap[w[0]].add(w[1:])
        # print(wordMap)

        res = 0
        for char1 in wordMap:
            # print(char1)
            for char2 in wordMap:
                # print(char2)
                if char1 == char2:
                    continue
                intersect = 0
                for w in wordMap[char1]:
                    # print(w)
                    if w in wordMap[char2]:
                        # print(w)
                        intersect += 1
                        # print(intersect)

                distinct1 = len(wordMap[char1]) - intersect
                # print(distinct1)
                # print(len(wordMap[char1]))
                distinct2 = len(wordMap[char2]) - intersect
                print(distinct2)
                res += distinct1*distinct2
                # print(res)
        return res

s = Solution()
a = s.distinctNames(["coffee","donuts","time","toffee"])
print(a)