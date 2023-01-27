class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        row_cnt = len(rooms)
        
        if row_cnt == 0:
            return 
        
        Directions = [(1,0),(-1,0),(0,1),(0,-1)]
        ROOM,GATE = (1 << 31) - 1, 0
        col_cnt = len(rooms[0])
        queue = collections.deque()
        
        for row in range(row_cnt):
            for col in range(col_cnt):
                if rooms[row][col] == GATE:
                    queue.append((row,col))
                    
                    
        while queue:
            cur_row,cur_col = queue.popleft()
            
            for dr,dx in Directions:
                next_row = cur_row + dr
                next_col = cur_col + dx
                
                if 0 <= next_row < row_cnt and 0 <= next_col < col_cnt \
                and rooms[next_row][next_col] == ROOM:
                    rooms[next_row][next_col] = rooms[cur_row][cur_col] + 1
                    queue.append((next_row,next_col))