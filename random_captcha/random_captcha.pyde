import os
import random

user_input = []
message = ""

def draw():
    fill(255)
    noStroke()
    rect(0, 315, 355, 160)
    
    fill(0)
    text("Wpisz kod za pomoca strzalek:", 40, 300)
        
    text(" ".join(user_input), 40, 340)
        
    fill(0, 150, 0)
    text(message, 40, 380)

def keyPressed():
    global user_input, message
    
    if keyCode == UP:
        user_input.append("UP")
    elif keyCode == DOWN:
        user_input.append("DOWN")
    elif keyCode == LEFT:
        user_input.append("LEFT")
    elif keyCode == RIGHT:
        user_input.append("RIGHT")
    elif key == BACKSPACE or key == DELETE:
        user_input = []
    elif key == ENTER:
        if user_input == correct_code:
            message = "Kod poprawny!"
        else:
            message = "Kod niepoprawny. Sproboj ponownie."
        user_input = []



def setup():
    background(255)
    size(355, 475)
    textAlign(width/3, height/3)
    textSize(20)
    folder_path = 'C:/Users/jturo/Pulpit/random_captcha/Images'  ##### ŚCIEŻKA FOLDERU- DO ZMIANY
    display_random_image_from_folder(folder_path)
    

def display_random_image_from_folder(folder_path):
    #lista plików
    files = os.listdir(folder_path)
    #rozszerzenia plików
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
    images = [f for f in files if os.path.splitext(f)[1].lower() in image_extensions]
    #losowy obraz
    random_image = random.choice(images)
    image_path = os.path.join(folder_path, random_image)
    #wyswietlanie obrazu
    img = loadImage(image_path)
    image(img, 0, 0)
    print(image_path)
    print(random_image)

    global correct_code
    if random_image == "captcha1.png":
        correct_code = ["LEFT", "LEFT", "UP", "UP", "RIGHT"]
    elif random_image == "captcha2.png":
        correct_code = ["RIGHT", "RIGHT", "RIGHT", "RIGHT", "RIGHT"]
    elif random_image == "captcha3.png":
        correct_code = ["LEFT", "DOWN", "RIGHT", "UP", "UP"]
    elif random_image == "captcha4.png":
        correct_code = ["LEFT", "RIGHT", "RIGHT", "LEFT", "RIGHT"]
    
