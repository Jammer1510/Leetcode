class Solution:
    
    
    cache = dict()
    
    def fib(self, n: int) -> int:
        
        
        
        if n in self.cache:
            return self.cache[n]
        
        if n < 2:
            result = n
        else:
            result = self.fib(n-1) + self.fib(n-2)
            
        self.cache[n] = result 
        return result