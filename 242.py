from collections import Counter
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         a = Counter(s)
#         b = Counter(t)     
#                                                 # return Counter(s) == Counter(t)
#         if a == b:
#             return True
#         return False


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         for index in set(s):
#             if s.count(index) != t.count(index):
#                 return False
        
#         return True


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s)==sorted(t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS,countT = {},{}
        for i in range(len(s)):
            countS[s[i]] = 1+countS.get(s[i],0)
            print(countS[s[i]])
            # print(countS)
            countT[t[i]] = 1+countS.get(t[i],0)
            # print(countT)

        return countT == countS



s = Solution()
a = s.isAnagram("anagram","nagaram")
print(a)