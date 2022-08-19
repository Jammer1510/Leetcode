class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(left:int,right:int,s:str) -> None:
            
            if len(s) == n*2:
                res.append(s)
                return
            else:
                
                if left<n:
                    backtrack(left+1,right,s + "(")
                    
                if left>right:
                    backtrack(left,right+1,s + ")")
                    
        backtrack(0,0,"")
        return res