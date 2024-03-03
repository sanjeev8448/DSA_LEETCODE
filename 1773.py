from typing import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        keys_dict = {"type":0,"color":1,"name":2}

        res = 0

        index_ = keys_dict[ruleKey]
        print(index_)
        for i in items:
            if i[index_] == ruleValue:
                print(i[index_])
                res+=1

        return res
    
s = Solution()
x = s.countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]],"color","silver")
print(x)
