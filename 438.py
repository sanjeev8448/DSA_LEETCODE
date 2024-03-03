from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        pCount,sCount = {},{}
        for i in range(len(p)):
            pCount[p[i]] = 1+pCount.get(p[i],0)
            # print(pCount)
            sCount[s[i]] = 1+sCount.get(s[i],0)
            # print(sCount)
        
        res = [0] if sCount == pCount else []
        # print(res)
        l = 0
        for r in range(len(p),len(s)):
            sCount[s[r]] = 1+sCount.get(s[r],0)
            print(sCount)
            sCount[s[l]] -= 1
            # print(sCount)

            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l+=1
            if sCount==pCount:
                res.append(l)
        return res
s = Solution()
a = s.findAnagrams("cbaebabacd","abc")
print(a)


        
        # startIndex = 0
        # pMap, sMap = {}, {}
        # res = []
        
        # for char in p:
        #     pMap[char] = 1 + pMap.get(char, 0)
        #     # print(pMap)
        
        # for i in range(len(s)):
        #     sMap[s[i]] = 1 + sMap.get(s[i], 0)
        #     # print(sMap)

        #     if i >= len(p) - 1:
        #         if sMap == pMap:
        #             res.append(startIndex)

                
        #         # If current character is in sMap, remove it and re-update the map.
        #         if s[startIndex] in sMap:
        #             sMap[s[startIndex]] -= 1
        #             print(sMap)
        #             if sMap[s[startIndex]] == 0:
        #                 del sMap[s[startIndex]]
        #         startIndex += 1
        
        # return res


# s = Solution()
# a = s.findAnagrams("cbaebabacd","abc")
# print(a)