class Solution:
    def countBits(num):
        count = 0
        
        while num > 0:
            count += 1
            num &= (num - 1)  # Clear the least significant set bit.
        
        return count

    def sortByBits(self, arr):
        arr.sort(key = lambda num: (Solution.countBits(num), num))
        return arr
    
s = Solution()
a = s.sortByBits([0,1,2,3,4,5,6,7,8]) 
print(a)