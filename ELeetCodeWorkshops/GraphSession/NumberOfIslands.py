class Solution:   
    def dfs(self, cell: tuple, grid: List[List[str]], visited: set):
        rows = len(grid)
        cols = len(grid[0])
        visited.add(cell)
        x, y = cell
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        for dx, dy in directions:
            newX = x + dx
            newY = y + dy
            if 0 <= newX and newX < cols and 0 <= newY and newY < rows:
                if grid[newY][newX] == "1" and (newX,newY) not in visited:
                    self.dfs((newX,newY), grid, visited)


    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        visited = set()

        for y in range(rows):
            for x in range(cols): 
                if grid[y][x] == "1" and (x,y) not in visited:
                    count += 1
                    self.dfs((x,y),grid,visited)

        return count