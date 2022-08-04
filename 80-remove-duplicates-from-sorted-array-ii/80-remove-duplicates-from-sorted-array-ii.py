class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        j = 0
        count = 1
        
        for i in range(1,len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
                count = 1
            else:
                if count != 2:
                    j += 1
                    nums[j] = nums[i]
                    count += 1
                
        return j + 1