class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        if len(nums) == 0:
            if upper == lower:
                return [str(lower)]
            return [str(lower) + "->" + str(upper)]
            
        if lower < nums[0]:
                nums.insert(0, lower - 1)
                
        if upper > nums[-1]:
                nums.append(upper + 1)
                
        output = []
            
        for i in range(1, len(nums)):
            difference = nums[i] - nums[i - 1]
            if difference > 2:
                output.append(str(nums[i - 1] + 1) + "->" + str(nums[i] -1))
                    
            elif difference == 2:
                output.append(str(nums[i -1] + 1))
                    
        return output
                    
