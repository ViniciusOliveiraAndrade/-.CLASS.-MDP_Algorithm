from UI import UI

class MDP(object):
    def __init__(self, ui_width, ui_height, number = 1, r = -0.4):
        self.ui_width=ui_width
        self.ui_height=ui_height
        self.number = number
        self.ui = UI(ui_width, ui_height, plus = ui_width * number, r = r)

    def display(self):
        self.ui.display()
        # text("POLICY:", )
