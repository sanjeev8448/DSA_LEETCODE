class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # usnig Two Pointers

        i,j = 0,0
        res = ""

        while i<len(word1) and j<len(word2):
            res += word1[i]+word2[j]  
            i+=1
            j+=1

        return res + word1[i:] + word2[j:]