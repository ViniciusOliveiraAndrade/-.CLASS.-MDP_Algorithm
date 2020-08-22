class Cell (object):
    def __init__(self, i, j, u=0, terminal=False):
        self.i = i
        self.j = j
        self.u = u
        self.terminal = terminal

    def getUpNeighbor(self):
        # print(self.i,self.j)
        neighborList = []
        if self.j-1 < 0:
            neighborList.append([self.i, self.j, 0.1])
            neighborList.append([self.i, self.j+1, 0.1])

        elif self.j+1 > 3:
            neighborList.append([self.i, self.j-1, 0.1])
            neighborList.append([self.i, self.j, 0.1])

        else:
            neighborList.append([self.i, self.j-1, 0.1])
            neighborList.append([self.i, self.j+1, 0.1])

        if self.i - 1 < 0:
            neighborList.append([self.i, self.j, 0.8])
        else:
            neighborList.append([self.i-1, self.j, 0.8])

        return neighborList

    def getDownNeighbor(self):
        neighborList = []
        if self.j-1 < 0:
            neighborList.append([self.i, self.j, 0.1])
            neighborList.append([self.i, self.j+1, 0.1])

        elif self.j+1 > 3:
            neighborList.append([self.i, self.j-1, 0.1])
            neighborList.append([self.i, self.j, 0.1])

        else:
            neighborList.append([self.i, self.j-1, 0.1])
            neighborList.append([self.i, self.j+1, 0.1])

        if self.i + 1 > 2:
            neighborList.append([self.i, self.j, 0.8])
        else:
            neighborList.append([self.i+1, self.j, 0.8])

        return neighborList

    def getRightNeighbor(self):
        neighborList = []
        if self.i-1 < 0:
            neighborList.append([self.i, self.j, 0.1])
            neighborList.append([self.i+1, self.j, 0.1])

        elif self.i+1 > 2:
            neighborList.append([self.i - 1, self.j, 0.1])
            neighborList.append([self.i, self.j, 0.1])

        else:
            neighborList.append([self.i-1, self.j, 0.1])
            neighborList.append([self.i+1, self.j, 0.1])

        if self.j + 1 > 3:
            neighborList.append([self.i, self.j, 0.8])
        else:
            neighborList.append([self.i, self.j + 1, 0.8])

        return neighborList

    def getLeftNeighbor(self):
        neighborList = []
        if self.i-1 < 0:
            neighborList.append([self.i, self.j, 0.1])
            neighborList.append([self.i+1, self.j, 0.1])

        elif self.i+1 > 2:
            neighborList.append([self.i - 1, self.j, 0.1])
            neighborList.append([self.i, self.j, 0.1])

        else:
            neighborList.append([self.i-1, self.j, 0.1])
            neighborList.append([self.i+1, self.j, 0.1])

        if self.j - 1 < 0:
            neighborList.append([self.i, self.j, 0.8])
        else:
            neighborList.append([self.i, self.j-1, 0.8])

        return neighborList




# class Cell(object):
#     def __init__(self, i, j, u = 0, cellType = False, plus = 0, s = 40):
#         self.i = i
#         self.j = j
#         self.u = u
#         self.cellType = cellType
#         self.plus = plus
#         self.s = s
    
#     def getX(self):
#         return ((self.j * self.s) + self.plus)
#     def getY(self):
#         return self.i * self.s
    
#     def display(self):
#         # noStroke()
#         stroke(255)
#         strokeWeight(2)
#         fill(255,255,255,100)
#         rect(self.getX(), self.getY(), self.s, self.s)
#         if self.cellType:
#             rect(self.getX()+6, self.getY()+6, self.s-12, self.s-12)
#         fill(255,255,255)
#         text("{0:.5f}".format(self.u),self.getX()+(self.s / 6),self.getY() + (self.s /2))
