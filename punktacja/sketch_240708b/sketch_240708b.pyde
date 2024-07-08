import random

kropki = []

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
        self.trajektoria_x = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        self.trajektoria_y = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])

    def update(self):
        if self.y >= Wekranu or self.y <= 0:
            self.kierunek_wys *= -1

        self.x += self.trajektoria_x * self.kierunek_szer
        self.y += self.trajektoria_y * self.kierunek_wys

        rect(self.x, self.y, self.wielkosc, self.wielkosc)

    def get_pos_x(self):
        return self.x

    def get_pos_y(self):
        return self.y

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
    global lewaPlatforma, prawaPlatforma, pilka, kropki, lewa_punkty, prawa_punkty
    lewaPlatforma = Platforma(0, Wekranu / 2 - wysokoscPlatformy / 2)
    prawaPlatforma = Platforma(Szekranu - szerokoscPlatformy, Wekranu / 2 - wysokoscPlatformy / 2)
    pilka = Pilka()
    lewa_punkty = 0
    prawa_punkty = 0
    size(Szekranu, Wekranu)
    frameRate(80)

def draw():
    global lewaPlatforma, prawaPlatforma, pilka, kropki, lewa_punkty, prawa_punkty
    background(0)  # czarne tło
    lewaPlatforma.display()
    prawaPlatforma.display()
    pilka.update()

    # Sprawdzanie kolizji piłki z platformami
    if pilka.get_pos_x() <= lewaPlatforma.get_pos_x() + szerokoscPlatformy:
        if lewaPlatforma.get_pos_y() <= pilka.get_pos_y() <= lewaPlatforma.get_pos_y() + wysokoscPlatformy:
            pilka.kierunek_szer *= -1
    if pilka.get_pos_x() + pilka.wielkosc >= prawaPlatforma.get_pos_x():
        if prawaPlatforma.get_pos_y() <= pilka.get_pos_y() <= prawaPlatforma.get_pos_y() + wysokoscPlatformy:
            pilka.kierunek_szer *= -1

    # Sprawdzanie, czy piłka przekroczyła krawędzie ekranu
    if pilka.get_pos_x() <= 0:
        prawa_punkty += 1
        pilka.reset_pilki()
    elif pilka.get_pos_x() + pilka.wielkosc >= Szekranu:
        lewa_punkty += 1
        pilka.reset_pilki()

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
