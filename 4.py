# Time: log(min(n, m))
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        # print(total)
        half = total // 2
        # print(half)                                     

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        # print(l)
        # print(r)
        while True:
            i = (l + r) // 2  # A
            # print(i)
            j = half - i - 2  # B
            # print(j)
            # print("new thing")

            Aleft = A[i] if i >= 0 else float("-infinity")
            # print(Aleft)
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            # print(Aright)
            Bleft = B[j] if j >= 0 else float("-infinity")
            # print(Bleft)
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
            # print(Bright)

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1


s = Solution()
a = s.findMedianSortedArrays([1,2],[3,4])
print(a)

# print(-1//2)