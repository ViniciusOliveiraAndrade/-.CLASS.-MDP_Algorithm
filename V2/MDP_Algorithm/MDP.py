from Cell import Cell
from UI import UI

class MDP (object):

    def __init__(self, r, ui_width, ui_height, number = 1):
        self.r = r
        
        self.start()
        
        self.ui_width=ui_width
        self.ui_height=ui_height
        self.number = number
        
        self.ui = UI(ui_width, ui_height, plus = ui_width * number)
    
    def start(self):
        self.gridInit()
        self.policyInit()  
        self.aux_gridInit()
                
    def policyInit(self):
        self.policy = []
        for i in range(3):
            self.policy.append([])
            for j in range(4):
                self.policy[i].append("*")
    
    def gridInit(self):
        self.grid = []
        
        self.generateMatriz()
        
        self.grid[0][3].u = 1
        self.grid[0][3].terminal = True
        self.grid[1][3].u = -1
        self.grid[1][3].terminal = True
        self.grid[2][3].r = 0.2
        self.grid[1][1].r = -0.5
        # self.grid[1][1].terminal = True

    def generateMatriz(self):
        for i in range(3):
            self.grid.append([])
            for j in range(4):
                cell = Cell(i, j,self.r)
                self.grid[i].append(cell)
                
    def aux_gridInit(self):
        
        self.generateMatriz2()
        
        self.aux_grid[0][3].u = 1
        self.aux_grid[0][3].terminal = True
        self.aux_grid[1][3].u = -1
        self.aux_grid[1][3].terminal = True
        self.aux_grid[2][3].r = 0.2
        self.aux_grid[1][1].r = -0.5
        # self.grid[1][1].terminal = True
    
    
    def generateMatriz2(self):
        self.aux_grid = []
        for i in range(3):
            self.aux_grid.append([])
            for j in range(4):
                cell = Cell(i, j, self.r)
                self.aux_grid[i].append(cell)

    def update(self):
        for j in range(4):
            for i in reversed(range(3)):
                self.maxUtility(i, j)
        self.update_aux();

    def maxUtility(self, i,j):
        aux_cell = self.aux_grid[i][j]
        cell = self.grid[i][j]
        if not cell.terminal:
            maxUtility, action = self.max(i, j)
            print(cell.r, maxUtility)
            aux_cell.u = cell.r + maxUtility
            self.policy[i][j] = action

    def update_aux(self):
        for j in range(4):
            for i in reversed(range(3)):
                self.grid[i][j].u = self.aux_grid[i][j].u

    def max(self, i, j):
        cell = self.grid[i][j]
        upN = cell.getUpNeighbor()
        rightN = cell.getRightNeighbor()
        downN = cell.getDownNeighbor()
        leftN= cell.getLeftNeighbor()

        action = ["UP", "RIGHT", "DOWN", "LEFT"]
        aux = [self.utility(upN), self.utility(rightN), self.utility(downN), self.utility(leftN)]
        index = 0
        i = 0
        while i < 3:
            if aux[index] < aux[i+1]:
                index = i + 1
            i = i + 1
        return aux[index], action[index]

    def utility(self, neighbors):
        total = 0
        for neighbor in neighbors:
            cell = self.grid[neighbor[0]][neighbor[1]]
            total = (cell.u * neighbor[2]) + total
        return total

    def display(self):
        self.ui.display(self.grid, self.policy, self.r)
