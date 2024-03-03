from typing import List
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            # print(count)
            for c in s:
                count[ord(c) - ord("a")] += 1
            # print(count)
            ans[tuple(count)].append(s)
            # print(count)
            # print(ans)
        return ans.values()


# another code--

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         ans = {}
#         for anagram in strs:
#             sortedword = ''.join(sorted(anagram))
#             # print(sortedword)
#             if sortedword not in ans:
#                 ans[sortedword] = [anagram]
#                 # print(ans)
#             else:
#                 ans[sortedword].append(anagram)
#                 print(ans)
            
#         return ans.values()

s = Solution()
a = s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(a)
        


        