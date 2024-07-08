import random 

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
            
class Pilka():
    def __init__(self):
        self.x = width/2
        self.y = height/2
        self.kierunek_wys = 1
        self.kierunek_szer = 1
        self.trajektoria_x = 2
        self.trajektoria_y = 2
        
    def reset_pilki(self):
        self.x = width / 2
        self.y = height / 2
        trajektoria_x = random.choice([-5, -4, -3, -1, -2, 1, 2, 3, 4])
        trajektoria_y = random.choice([-5, -4, -3, -1, -2, 1, 2, 3, 4])
        
    def update(self):
        if self.y == height or self.y < 0:
            self.kierunek_wys = self.kierunek_wys* -1
        
        if self.x == width:
            self.reset_pilki()
            
        #if self.x - x == 5: # dotyka platformy
        #    self.kierunek_szer = -1
            
        self.x += self.trajektoria_x*self.kierunek_szer
        self.y += self.trajektoria_y*self.kierunek_wys
            
        rect(self.x, self.y, 20, 20) # kwadratowa pilka

def setup():
    global lewaPlatforma, prawaPlatforma, pilka
    lewaPlatforma = Platforma(0, Wekranu/ 2 - wysokoscPlatformy/ 2)
    prawaPlatforma = Platforma(Szekranu - szerokoscPlatformy, Wekranu/ 2 - wysokoscPlatformy/ 2)
    pilka = Pilka()
    iteracja_programu = 0
    size(Szekranu, Wekranu)
    frameRate(80)
    
def draw():
    global iteracja_programu, lewaPlatforma, prawaPlatforma, pilka
    #iteracja_programu +=1
    rect(0, 0, width, height) # background
    lewaPlatforma.display()
    prawaPlatforma.display()
    pilka.update() 
    
    if keyPressed:
        if key == 'w':
            lewaPlatforma.move('up')
        elif key == 's':
            lewaPlatforma.move('down')
        
        if keyCode == UP:
            prawaPlatforma.move('up')
        elif keyCode == DOWN:
            prawaPlatforma.move('down')
            
