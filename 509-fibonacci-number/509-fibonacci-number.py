class Solution:
    def fib(self, n: int) -> int:
        
        cache = dict()
        
        if n in cache:
            return cache[n]
        
        if n < 2:
            result = n
        else:
            result = self.fib(n-1) + self.fib(n-2)
            
        cache[n] = result 
        return result