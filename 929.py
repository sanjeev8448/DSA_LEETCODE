from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for e in emails:
            i,local = 0,""
            # print(e[i])
            while e[i] not in ['@','+']:
                if e[i] != ".":
                    local+=e[i]
                i+=1
            print(local)

            while e[i] != '@':
                i+=1
            domain = e[i+1:]
            unique.add((local,domain))
        
        return len(unique)
    
s = Solution()
res = s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
print(res)