from typing import List
# class Solution:
#     def compress(self, chars: List[str]) -> int:
#         i = 0
#         index = 0 # to write into the original array

#         while i<len(chars):
#             j = i
#             # print(i)
#             # print(j)
#             while j<len(chars) and chars[j] == chars[i]:
#                 j+=1
#                 # print(j)
#             chars[index] = chars[i]
#             print(chars[index])
#             index += 1

#             count = j-i
#             if count > 1: 
#                 for c in str(count):
#                     chars[index] = c
#                     index += 1

#             i = j
            
#         chars = chars[:index]
#         # print(chars)
#         return index

class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 1:
            return 1
        
        i = 0
        j = 0
        
        while i < n:
            count = 1
            while i < n - 1 and chars[i] == chars[i+1]:
                count += 1
                i += 1
            
            chars[j] = chars[i]
            j += 1
            
            if count > 1:
                for c in str(count):
                    chars[j] = c
                    j += 1
            
            i += 1
        
        return j

s = Solution()
a = s.compress(["a","a","b","b","c","c","c"])
print(a)