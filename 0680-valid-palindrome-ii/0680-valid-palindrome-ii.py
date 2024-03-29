class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Write your code here
        if s is None:
            return False

        left,right = self.findDifference(s,0,len(s) - 1)
        if left >= right:
            return True
            
        return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1) 



    
    def isPalindrome(self,s,left,right):
        left,right = self.findDifference(s,left,right)
        return left >= right

    def findDifference(self,s,left,right):
        while left < right:
            if s[left] != s[right]:
                return left,right
            left += 1
            right -= 1
        return left,right
        
        
        
        
        