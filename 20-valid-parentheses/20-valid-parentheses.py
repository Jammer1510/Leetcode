from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        
        mappings = dict()
        mappings["]"] = "["
        mappings["}"] = "{"
        mappings[")"] = "("
        
        for i in range(len(s)):
            curChar = s[i]
            
            if curChar in mappings:
                if len(stack) == 0:
                    return False
                    
                openingBrackets = stack.pop()
                
                if openingBrackets != mappings[curChar]:
                    return False
                    
            else:
                stack.append(curChar)
                
        return len(stack) == 0