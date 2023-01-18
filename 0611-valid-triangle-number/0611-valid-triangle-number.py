class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res = 0 
        nums.sort()
        if not nums or len(nums) < 3:
            return res
        for i in range(2,len(nums)):
            res += self.count(nums,i)
        return res
    
    def count(self,ls,target):
        counter = 0
        left = 0
        right = target - 1
        targetSum = ls[target]
        
        while left < right:
            if ls[left] + ls[right] > targetSum:
                counter += right - left
                right -= 1
            else:
                left += 1
        return counter
        