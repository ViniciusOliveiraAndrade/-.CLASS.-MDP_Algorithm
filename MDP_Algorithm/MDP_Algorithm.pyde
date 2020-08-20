from MDP import MDP

def setup():
    global mdpA, mdpB, mdpC
    size(900, 403)
    mdpA = MDP(width, height, 0)
    mdpB = MDP(width, height, 1)
    mdpC = MDP(width, height, 2)
    
    
def draw():
    background(51)
    mdpA.display()
    mdpB.display()
    mdpC.display()
