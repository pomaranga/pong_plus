class Platforma:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.szerokosc = szerokoscPlatformy
        self.wysokosc = wysokoscPlatformy
        self.predkosc = predkoscPlatformy
        
    def display(self):
        rect(self.x, self.y, self.szerokosc, self.wysokosc)
        
    def move(self, kierunek):
        if kierunek == 'up' and self.y > 0:
            self.y -= self.predkosc
        elif kierunek == 'down' and self.y < Wekranu - self.wysokosc:
            self.y += self.predkosc
            
Szekranu = 800
Wekranu = 600

szerokoscPlatformy = 10
wysokoscPlatformy = 100
predkoscPlatformy = 5
            
lewaPlatforma = Platforma(0, Wekranu/ 2 - wysokoscPlatformy/ 2)
prawaPlatforma = Platforma(Szekranu - szerokoscPlatformy, Wekranu/ 2 - wysokoscPlatformy/ 2)


def setup():
    global iteracja_programu
    iteracja_programu = 0
    size(Szekranu, Wekranu)
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
    lewaPlatforma.display()
    prawaPlatforma.display()
    
    if keyPressed:
        if key == 'w':
            lewaPlatforma.move('up')
        elif key == 's':
            lewaPlatforma.move('down')
        
        if keyCode == UP:
            prawaPlatforma.move('up')
        elif keyCode == DOWN:
            prawaPlatforma.move('down')
            
