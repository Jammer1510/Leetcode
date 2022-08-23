class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        if not grid or not grid[0]:
            return 0
        
        count = 0
        
                
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] =='1':
                    count += 1
                    self.dfs(grid, i, j)
                    
        
        return count
    
    #bfs
    def bfs(self,grid,i,j):
        q = deque([(i,j)])
        grid[i][j] = '@'
        
        while q:
            grid[i][j] = q.popleft()
            for delta_i,delta_j in [(-1,0),(1,0),(0,-1),(0,1)]:
                next_i = i + delta_i
                next_j = j + delta_j
                
                if next_i < 0 or next_j < 0 or next_i >= len(grid) or next_j >= len(grid[0]) or grid[next_i][next_j] == '1':
                    continue
                
                q.append((next_i,next_j))
                grid[i][j] = '@'
        
    #dfs 
    def dfs(self,grid, i, j):            
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
                return
            
            grid[i][j] = '@'
            
            self.dfs(grid, i + 1, j)
            self.dfs(grid, i - 1, j)
            self.dfs(grid, i, j - 1)
            self.dfs(grid, i, j + 1)