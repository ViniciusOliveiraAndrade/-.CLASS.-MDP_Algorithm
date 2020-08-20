class UI(object):
    def __init__(self, screen_width, screen_height, plus = 0, r = -0.4):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.plus = plus
        self.r = r
        
        self.generateGrid()
        
        self.grid[0][3].value = 1
        self.grid[0][3].cellType = True
        
        self.grid[1][3].value = -1
        self.grid[1][3].cellType = True
        
        self.grid[2][3].value = 0.2
        
        self.grid[1][1].value = -0.5
        
    def generateGrid(self):
        self.grid = []
        s = self.screen_width / 4
        for i in range(3):
            self.grid.append([])
            for j in range(4):
                cell = Cell(i, j,value = self.r, plus = self.plus, s = s)
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
        
    
class Cell(object):
    def __init__(self, i, j, value = 0, cellType = False, plus = 0, s = 40):
        self.i = i
        self.j = j
        self.value = value
        self.cellType = cellType
        self.plus = plus
        self.s = s
    
    def getX(self):
        return ((self.j * self.s) + self.plus)
    def getY(self):
        return self.i * self.s
    
    def display(self):
        # noStroke()
        stroke(255)
        strokeWeight(2)
        fill(255,255,255,100)
        rect(self.getX(), self.getY(), self.s, self.s)
        if self.cellType:
            rect(self.getX()+6, self.getY()+6, self.s-12, self.s-12)
        fill(255,255,255)
        text("{0:.5f}".format(self.value),self.getX()+(self.s / 6),self.getY() + (self.s /2))
