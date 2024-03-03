from typing import List
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num.reverse()
        i = 0
        while k:
            digit = k % 10
            if i < len(num):
                num[i] += digit
            else:
                num.append(digit)
            
            carry = num[i] // 10
            num[i] = num[i] % 10

            k = k // 10
            k += carry
            i += 1
        num.reverse()
        return num

s = Solution()
a = s.addToArrayForm([2,1,5],806)       
# a = s.addToArrayForm([1,2,0,0],34) 
print(a)