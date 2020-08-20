from MDP import MDP

def setup():
    global mdpA, mdpB, mdpC
    size(900, 403)
    UISIZE = width / 3
    mdpA = MDP(UISIZE, height, 0)
    mdpB = MDP(UISIZE, height, 1,r=-0.04)
    mdpC = MDP(UISIZE, height, 2,r=-0.0004)
    
    
def draw():
    background(51)
    mdpA.display()
    mdpB.display()
    mdpC.display()
    
def keyTyped():
    if key == ' ':
        pass
