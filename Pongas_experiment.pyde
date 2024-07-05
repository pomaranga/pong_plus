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
    global lewaPlatforma, prawaPlatforma, xpos, ypos, kierunek_pilki1, kierunek_pilki2, trajektoriax, trajektoriay
    lewaPlatforma = Platforma(0, Wekranu/ 2 - wysokoscPlatformy/ 2)
    prawaPlatforma = Platforma(Szekranu - szerokoscPlatformy, Wekranu/ 2 - wysokoscPlatformy/ 2)
    xpos = width/2
    ypos = height/2
    import random
    kierunek_pilki1 = random.choice([-1, -2, -3, 1, 2, 3])
    kierunek_pilki2 = random.choice([-1, -2, -3, 1, 2, 3])
    trajektoriax = 2
    trajektoriay = 2
    size(Szekranu, Wekranu)
    frameRate(60)
    
def draw():
    global iteracja_programu, lewaPlatforma, prawaPlatforma
    global xpos, ypos,  trajektoriax, trajektoriay, kierunek_pilki1, kierunek_pilki2, reset_pilki
    #iteracja_programu +=1
    

    
    if ypos == height or ypos < 0:
        kierunek_pilki2 = kierunek_pilki2* -1
    rect(0, 0, width, height) # background
    
    if xpos == width or xpos <0:
        reset_pilki()
    
    
    def reset_pilki():
        global xpos, ypos, trajektoriax, trajektoriay
        xpos = width / 2
        ypos = height / 2
        import random 
        trajektoriax = random.choice([-1, -2, 1, 2, 3])
        trajektoriay = random.choice([-3, -1, -2, 1, 2, 3, 4])
    
    rect(xpos, ypos, 20, 20)
    
    xpos += trajektoriax*kierunek_pilki1
    ypos += trajektoriay*kierunek_pilki2
    
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
            
