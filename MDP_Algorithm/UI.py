class UI(object):
    def __init__(self, screen_width, screen_height, plus = 0):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.plus = plus
        self.r = r
        
        self.generateGrid()
        
        self.grid[0][3].u = 1
        self.grid[0][3].cellType = True
        
        self.grid[1][3].u = -1
        self.grid[1][3].cellType = True
        
        self.grid[2][3].u = 0.2
        
        self.grid[1][1].u = -0.5
        
    def generateGrid(self):
        self.grid = []
        s = self.screen_width / 4
        for i in range(3):
            self.grid.append([])
            for j in range(4):
                cell = Cell(i, j, plus = self.plus, s = s)
                self.grid[i].append(cell)
                                            
    def checkNeighbors(self, current_cell):
        neighbors = []
        return None
                
    def getNeighbors(self, gridPoint):
        neighbors = []
        return []
    
    def display(self):
        for rows in self.grid:
            for cell in rows:
                cell.display()
        stroke(0, 102, 255)     
        strokeWeight(3)
        line(self.plus, 0, self.plus, self.screen_height)
        line(self.screen_width + self.plus, 0, self.screen_width + self.plus, self.screen_height)
