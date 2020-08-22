class Cell (object):
    def __init__(self, i, j, u=0, terminal=False):
        self.i = i
        self.j = j
        self.u = u
        self.terminal = terminal

    def getUpNeighbor(self):
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
