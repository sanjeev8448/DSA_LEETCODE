from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        def isPrefixAndSuffix(str1,str2):
            if len(str1) <= len(str2):
                print(str1[:])
                print(str2[:len(str1)])
                print(str2[-len(str1):])
                if str1[:] == str2[:len(str1)] and str1[:] == str2[-len(str1):]:
                    return True
            return False
                
        
        res = 0
        
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if isPrefixAndSuffix(words[i],words[j]):
                    res += 1
        return res
    
 
s = Solution()
res = s.countPrefixSuffixPairs(["bb","bb"])
print(res)