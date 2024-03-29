class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        start,end = 0, len(nums) -1 
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if nums[mid] < nums[mid - 1]:
                end = mid
            elif nums[mid] < nums[mid + 1]:
                start = mid
            else:
                return mid
        return end if nums[start] < nums[end] else start