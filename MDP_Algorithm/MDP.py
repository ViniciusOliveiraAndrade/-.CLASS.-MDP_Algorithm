from UI import UI

class MDP(object):
    def __init__(self, screen_width, screen_height, number = 1):
        UISIZE = screen_width/3
        self.ui = UI(screen_width/3, screen_height, plus = UISIZE * number)

    def display(self):
        self.ui.display()
