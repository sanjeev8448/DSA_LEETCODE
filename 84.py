# from typing import List
# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         maxArea = 0
#         stack = []  # pair: (index, height)

#         for i, h in enumerate(heights):
#             start = i
#             while stack and stack[-1][1] > h:
#                 index, height = stack.pop()
#                 maxArea = max(maxArea, height * (i - index))
#                 start = index
#             stack.append((start, h))
#             print(stack)

#         for i, h in stack:
#             maxArea = max(maxArea, h * (len(heights) - i))
#         return maxArea


# s = Solution()
# a = s.largestRectangleArea([2,1,5,6,2,3])
# print(a)
# print(9//2)

# n = 4
# if n % 2:
#     print("yes")
# else:
#     print('no')

for i in range(0,10,2):
    print(i)