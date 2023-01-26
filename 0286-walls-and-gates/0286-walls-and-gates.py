class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        row_count = len(rooms)
        
        if row_count == 0:
            return 
        
        Room,Gate = (1 << 31) - 1, 0
        DIRECTIONS = [(1,0),(-1,0),(0,-1),(0,1)]
        
        col_count = len(rooms[0])
        q = collections.deque()
        
        for row in range(row_count):
            for col in range(col_count):
                if rooms[row][col] == Gate:
                    q.append((row,col))

        while q:
            cur_row,cur_col = q.popleft()
            
            for dr,dc in DIRECTIONS:
                next_row = cur_row + dr
                next_col = cur_col + dc
                
            
                if 0 <= next_row < row_count and 0 <= next_col < col_count and \
                rooms[next_row][next_col] == Room:
                    rooms[next_row][next_col] = rooms[cur_row][cur_col] + 1                
                    q.append((next_row,next_col))
                    
        
        