import random

kropki = []

Szekranu = 800
Wekranu = 600

szerokoscPlatformy = 10
wysokoscPlatformy = 100
predkoscPlatformy = 6

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

    def get_pos_x(self):
        return self.x

    def get_pos_y(self):
        return self.y

class Pilka:
    def __init__(self):
        self.x = Szekranu / 2
        self.y = Wekranu / 2
        self.kierunek_wys = 1
        self.kierunek_szer = 1
        self.trajektoria_x = 2
        self.trajektoria_y = 2
        self.wielkosc = 20

    def reset_pilki(self):
        self.x = Szekranu / 2
        self.y = Wekranu / 2
        self.trajektoria_x = random.choice([-5, -4, -3, -2, 2, 3, 4, 5])
        self.trajektoria_y = random.choice([-5, -4, -3, -2, 2, 3, 4, 5])
    
        
    def update(self):
        if self.y >= Wekranu or self.y <= 0:
            self.trajektoria_y *= -1

        self.x += self.trajektoria_x
        self.y += self.trajektoria_y

        rect(self.x, self.y, self.wielkosc, self.wielkosc)

    def get_pos_x(self):
        return self.x

    def get_pos_y(self):
        return self.y
    
    #zmniejszanie prędkości piłki przy niektórych kątach
    def kontrola_predkosci():
        if self.trajektoria_x == 5 or self.trajketoria_y == 5 or self.trajektoria_x == -5 or self.trajektoria_y == -5:
            self.kierunek_szer = kierunek_pilki1* 0.2
            self.kierunek_wys = kierunek_pilki* 0.2
        
        if self.trajektoria_x == 4 or self.trajketoria_y == 4 or trajektoria_x == -4 or self.trajektoria_y == -4:
            self.kierunek_szer = kierunek_pilki1* 0.4
            self.kierunek_wys = kierunek_pilki* 0.4
            
class Kropka:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wielkosc = 40
        self.jest = True

    def display(self):
        if self.jest:
            ellipse(self.x, self.y, self.wielkosc, self.wielkosc)

    def kolizja(self, pilka):
        if (self.x - self.wielkosc / 2 <= pilka.get_pos_x() <= self.x + self.wielkosc / 2 and 
            self.y - self.wielkosc / 2 <= pilka.get_pos_y() <= self.y + self.wielkosc / 2):
            self.jest = False
            kropki.pop()
            
   
    

def setup():
    global lewaPlatforma, prawaPlatforma, pilka, kropki, lewa_punkty, prawa_punkty, kontrola_predkosci
    lewaPlatforma = Platforma(0, Wekranu / 2 - wysokoscPlatformy / 2)
    prawaPlatforma = Platforma(Szekranu - szerokoscPlatformy, Wekranu / 2 - wysokoscPlatformy / 2)
    pilka = Pilka()
    lewa_punkty = 0
    prawa_punkty = 0
    size(Szekranu, Wekranu)
    frameRate(80)

def draw():
    global lewaPlatforma, prawaPlatforma, pilka, kropki, lewa_punkty, prawa_punkty, kontrola_predkosci
    background(0)  # czarne tło
    lewaPlatforma.display()
    prawaPlatforma.display()
    pilka.update()

    # Sprawdzanie kolizji piłki z platformami
    if pilka.get_pos_x() <= lewaPlatforma.get_pos_x() + szerokoscPlatformy:
        if lewaPlatforma.get_pos_y() <= pilka.get_pos_y() <= lewaPlatforma.get_pos_y() + wysokoscPlatformy:
            pilka.trajektoria_x *= -1
    if pilka.get_pos_x() + pilka.wielkosc >= prawaPlatforma.get_pos_x():
        if prawaPlatforma.get_pos_y() <= pilka.get_pos_y() <= prawaPlatforma.get_pos_y() + wysokoscPlatformy:
            pilka.trajektoria_x *= -1
    
    if keyPressed:
        if key == 'w':
             if pilka.get_pos_x() <= lewaPlatforma.get_pos_x() + szerokoscPlatformy:
                 if lewaPlatforma.get_pos_y() <= pilka.get_pos_y() <= lewaPlatforma.get_pos_y() + wysokoscPlatformy:
                    if pilka.trajektoria_y < 0:
                         pilka.trajektoria_y *= 1.8
                    elif pilka.trajektoria_y > 0:
                         pilka.trajektoria_y *= 0.4
    #pilka zmienia predkość jeśli paletka rusza się gdy o nią uderzy            
    if keyPressed:
        if key == 's':
             if pilka.get_pos_x() <= lewaPlatforma.get_pos_x() + szerokoscPlatformy:
                 if lewaPlatforma.get_pos_y() <= pilka.get_pos_y() <= lewaPlatforma.get_pos_y() + wysokoscPlatformy:
                     if pilka.trajektoria_y < 0:
                         pilka.trajektoria_y *= 0.4
                     elif pilka.trajektoria_y > 0:
                         pilka.trajektoria_y *= 1.8
                    
    if keyPressed:
        if key == UP:
             if pilka.get_pos_x() <= prawaPlatforma.get_pos_x() + szerokoscPlatformy:
                 if prawaPlatforma.get_pos_y() <= pilka.get_pos_y() <= prawaPlatforma.get_pos_y() + wysokoscPlatformy:
                     if pilka.trajektoria_y < 0:
                         pilka.trajektoria_y *= 1.8
                     elif pilka.trajektoria_y > 0:
                         pilka.trajektoria_y *= 0.4
                
                    
    if keyPressed:
        if key == DOWN:
             if pilka.get_pos_x() <= prawaPlatforma.get_pos_x() + szerokoscPlatformy:
                 if prawaPlatforma.get_pos_y() <= pilka.get_pos_y() <= prawaPlatforma.get_pos_y() + wysokoscPlatformy:
                     if pilka.trajektoria_y < 0:
                         pilka.trajektoria_y *= 0.4
                     elif pilka.trajektoria_y > 0:
                         pilka.trajektoria_y *= 1.8
                
    
    # Sprawdzanie, czy piłka przekroczyła krawędzie ekranu
    if pilka.get_pos_x() <= 0:
        prawa_punkty += 1
        pilka.reset_pilki()
    elif pilka.get_pos_x() + pilka.wielkosc >= Szekranu:
        lewa_punkty += 1
        pilka.reset_pilki()
        
    print(pilka.trajektoria_x, pilka.trajektoria_y)

          
    fill(255)
    textSize(32)
    text(str(lewa_punkty), Szekranu / 4, 50)
    text(str(prawa_punkty), 3 * Szekranu / 4, 50)


    if frameCount % (5 * 60) == 0:  # prędkość pojawiania się kropek
        kropki.append(Kropka(random.randint(0, Szekranu), random.randint(0, Wekranu)))

    for kropka in kropki:
        kropka.display()
        kropka.kolizja(pilka)

    if keyPressed:
        if key == 'w':
            lewaPlatforma.move('up')
        elif key == 's':
            lewaPlatforma.move('down')

        if keyCode == UP:
            prawaPlatforma.move('up')
        elif keyCode == DOWN:
            prawaPlatforma.move('down')
            
    
    
        
