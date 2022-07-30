class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        totalRectangles = 0
        pairs = dict()
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    for x in range(j + 1, len(grid[i])):
                        if grid[i][x] == 1:
                            key = str(j) + "," + str(x)
                            if key in pairs:
                                totalRectangles += pairs[key]
                            else:
                                pairs[key] = 0
                            pairs[key] += 1
        
        return totalRectangles