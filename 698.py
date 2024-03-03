class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        if sum(nums) % k:
            return False
        
        nums.sort(reverse=True)
        # print(nums)
        target = sum(nums) / k
        used = [False]*len(nums)
        # print(used)

        def backtrack(i,k,subsetSum):
            if k == 0:
                return True

            if subsetSum == target:
                return backtrack(0,k-1,0)

            for j in range(i,len(nums)):
                if used[j] or subsetSum + nums[j] > target:
                    continue

                used[j] = True

                if backtrack(j+1,k,subsetSum + nums[j]):
                    return True

                used[j] = False

            return False

        return backtrack(0,k,0) 

s = Solution()
a = s.canPartitionKSubsets([4,3,2,3,5,2,1],4)
print(a)
    









        # if sum(nums) % k != 0:
        #     return False

        # nums.sort(reverse = True)
        # target = sum(nums) / k
        # visited= set()

        # def backtrack(idx, count, currSum):
        #     if count == k:
        #         return True

        #     if target == currSum:
        #         return backtrack(0, count + 1, 0)

        #     for i in range(idx, len(nums)):
                
        #         # skip duplicates if last same number was skipped
        #         if i > 0 and (i - 1) not in visited and nums[i] == nums[i - 1]:
        #             continue

        #         if i in visited or currSum + nums[i] > target:
        #             continue

        #         visited.add(i)

        #         if backtrack(i + 1, count, currSum + nums[i]):
        #             return True
                
        #         visited.remove(i)

        #     return False