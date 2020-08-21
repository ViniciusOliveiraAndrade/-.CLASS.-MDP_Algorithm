from MDP import MDP

def setup():
    global mdpA, mdpB, mdpC
    size(900, 403)
    UISIZE = width / 3
    mdpA = MDP(-0.4, UISIZE, height, 0)
    mdpB = MDP(-0.04, UISIZE, height, 1)
    mdpC = MDP(-0.0004, UISIZE, height, 2)
    
    
def draw():
    background(51)
    mdpA.display()
    mdpB.display()
    mdpC.display()
    
def keyTyped():
    if key == ' ':
        mdpA.update()
        mdpB.update()
        mdpC.update()
