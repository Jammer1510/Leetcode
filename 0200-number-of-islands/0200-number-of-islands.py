class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows,cols = len(grid),len(grid[0])
        visted = set()
        islands = 0
        
        def bfs(r,c):
            queue = collections.deque()
            visted.add((r,c))
            queue.append((r,c))

            while queue:
                row,col = queue.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr,dc in directions:
                    if ((row + dr)) in range(rows) and \
                    ((col + dc)) in range(cols) and \
                    grid[row + dr][col + dc] == "1" and (row + dr,col + dc) not in visted : \
                    queue.append((row + dr,col+ dc))
                    visted.add((row+dr,col+dc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visted:
                    bfs(r,c)
                    islands += 1
        return islands

        