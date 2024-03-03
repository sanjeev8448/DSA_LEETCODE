# from typing import List
# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         res = [[1]]

#         for i in range(numRows-1):
#             print(i)
#             temp = [0]+res[-1]+[0]
#             # print(temp)
#             row = []
#             for j in range(len(res[-1])+1):
#                 # print(j)
#                 row.append(temp[j]+temp[j+1])
#                 # print(row)
#             # print(row)
#             res.append(row)
#             # print(res)
#         return res

# s = Solution()
# a = s.generate(5)
# print(1//2)

lists = [[1,4,5],[1,3,4],[2,6]]
merge = [1,1,3,4,4,5]
# lists = merge
# print(len(lists))
for i in range(0,len(lists),2):
    print(lists[i])
if 3 < 3:
    print('ue')
else:
    print('no')
