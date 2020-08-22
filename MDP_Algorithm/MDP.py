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
        self.grid[2][3].u = 0.2
        self.grid[1][1].u = -0.5
        # self.grid[1][1].terminal = True

    def generateMatriz(self):
        for i in range(3):
            self.grid.append([])
            for j in range(4):
                cell = Cell(i, j)
                self.grid[i].append(cell)

    def update(self):
        for j in range(4):
            for i in reversed(range(3)):
                self.maxUtility(i, j)
        print (self.policy)

    def maxUtility(self, i,j):

        cell = self.grid[i][j]
        if not cell.terminal:
            maxUtility, action = self.max(i, j)
            cell.u = self.r + maxUtility
            self.policy[i][j] = action

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
        # print(aux, index)
        return aux[index], action[index]

    def utility(self, neighbors):
        total = 0
        for neighbor in neighbors:
            # print(neighbor[0],neighbor[1])
            cell = self.grid[neighbor[0]][neighbor[1]]
            total = (cell.u * neighbor[2]) + total
        return total

    def display(self):
        self.ui.display(self.grid, self.policy, self.r)
