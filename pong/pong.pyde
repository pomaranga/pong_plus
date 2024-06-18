Szekranu = 800
Wekranu = 600

szerokoscPlatformy = 10
wysokoscPlatformy = 100
predkoscPlatformy = 5

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

def setup():
    global iteracja_programu, lewaPlatforma, prawaPlatforma, xpos, ypos, kierunek_pilki
    lewaPlatforma = Platforma(0, Wekranu/ 2 - wysokoscPlatformy/ 2)
    prawaPlatforma = Platforma(Szekranu - szerokoscPlatformy, Wekranu/ 2 - wysokoscPlatformy/ 2)
    xpos = width/2
    ypos = height/2
    kierunek_pilki = 1
    iteracja_programu = 0
    size(Szekranu, Wekranu)
    frameRate(80)
    
def draw():
    global iteracja_programu, lewaPlatforma, prawaPlatforma
    global xpos, ypos, kierunek_pilki
    #iteracja_programu +=1
    if ypos > height:# or ypos<0:
        kierunek_pilki = kierunek_pilki* -1
    rect(0, 0, width, height) # background
    xpos += 1
    ypos += 1*kierunek_pilki
    #print(xpos, ypos, kierunek_pilki)
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
            
