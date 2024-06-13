def setup():
    global iteracja_programu
    iteracja_programu = 0
    size(1000, 600)
    frameRate(80)
    
def draw():
    global iteracja_programu
    iteracja_programu +=1
    global xpos
    xpos = 500 + iteracja_programu
    global ypos
    ypos = 300 + iteracja_programu
    rect(-5, -5, 5000, 5000)
    rect(xpos, ypos, 20, 20)
    
         
    
        

    
                   
        
        
