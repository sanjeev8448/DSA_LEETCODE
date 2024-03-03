from typing  import List
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # if len(nums) <= 2:
        #     return True
        changed = False
        # for i, num in enumerate(nums):
        #     if i == len(nums) - 1 or num <= nums[i + 1]:
        for i in range(len(nums)-1):
            if nums[i] <= nums[i+1]:
                continue
                # print(changed)

            if changed:
                # print(changed)
                return False
            
            if i == 0 or nums[i + 1] >= nums[i - 1]:
                nums[i] = nums[i + 1]
                # print(nums)
            else:
                nums[i + 1] = nums[i]
                print(nums)
            changed = True
        return True

s = Solution()
a = s.checkPossibility([3,4,2,3])
print(a)