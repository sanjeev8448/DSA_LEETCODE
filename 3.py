# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         charSet = set()
#         l = 0
#         res = 0

#         for r in range(len(s)):
#             while s[r] in charSet:
#                 charSet.remove(s[l])
#                 l+=1
#                 print(l)
#             charSet.add(s[r])
#             print(charSet)
#             res = max(res,r-l+1)
#             # print(res)

#         return res

# s = Solution()
# a = s.lengthOfLongestSubstring("pwwkew")
print(10%10)

