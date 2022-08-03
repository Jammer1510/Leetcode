class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        
        ans = 0
        leftmax = height[0]
        rightmax = height[-1]
        
        while i <= j:
            if height[i] <= height[j]:
                
                leftmax = max(leftmax ,height[i])
                ans += leftmax - height[i]
                i += 1
                    
            else:
                rightmax = max(rightmax ,height[j])  
                ans += rightmax - height[j]
                j -= 1
                    
        return ans