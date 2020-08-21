class UI(object):
    def __init__(self, screen_width, screen_height, plus = 0):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.plus = plus
    
    
    
    def display(self, grid):
        s = self.screen_width / 4
        for rows in grid:
            for cell in rows:
                
                x = (cell.j * s) + self.plus
                y = cell.i * s
                stroke(255)
                strokeWeight(2)
                fill(255,255,255,100)
                rect(x, y, s, s)
                if cell.terminal:
                    rect(x+6, y+6, s-12, s-12)
                fill(255,255,255)
                text("{0:.5f}".format(cell.u), x+(s / 6), y + (s /2))
        stroke(0, 102, 255)     
        strokeWeight(3)
        line(self.plus, 0, self.plus, self.screen_height)
        line(self.screen_width + self.plus, 0, self.screen_width + self.plus, self.screen_height)
