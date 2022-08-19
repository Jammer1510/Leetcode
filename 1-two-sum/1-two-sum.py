class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diff = dict()
        
        for i in range(len(nums)):
            if nums[i] in diff:
                return [diff[nums[i]], i]
            else:
                diff[target - nums[i]] = i
                
                