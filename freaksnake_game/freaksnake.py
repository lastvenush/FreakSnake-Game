import turtle
import time
import random
import os
import winsound

# Windows için masaüstü yolu
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop/freaksnake_game")

# Çalışma dizinini masaüstü olarak ayarla
os.chdir(desktop_path)

# Yeni çalışma dizinini yazdır
print("Current working directory:", os.getcwd())

# Ana menü fonksiyonu
def main_menu():
    window.clearscreen()  # Tüm ekranı temizle
    window.bgcolor("#E4CBFF")
    window.title("FreakSnake")
    window.addshape("assets/snake_head.gif")  # Görseli ekrana tanıt
    window.addshape("assets/bow.gif")  # Görseli ekrana tanıt
    window.addshape("assets/snake_image.gif")  # Görseli ekrana tanıt
    
    # Başlık
    title = turtle.Turtle()
    title.speed(0)
    title.color("black")
    title.penup()
    title.hideturtle()
    title.goto(0, 100)
    title.write("Welcome to FreakSnake", align="center", font=("Times New Roman", 24, "bold"))
    
    title_rightimage = turtle.Turtle()
    title_rightimage.speed(0)
    title_rightimage.shape("assets/bow.gif")
    title_rightimage.penup()
    title_rightimage.goto(220,130)
    
    title_leftimage = turtle.Turtle()
    title_leftimage.speed(0)
    title_leftimage.shape("assets/bow.gif")
    title_leftimage.penup()
    title_leftimage.goto(-220,130)
    
    snake_image = turtle.Turtle()
    snake_image.speed(0)
    snake_image.shape("assets/snake_image.gif")
    snake_image.penup()
    snake_image.goto(0,-150)

    # Play düğmesi
    play_button = turtle.Turtle()
    play_button.speed(0)
    play_button.shape("square")
    play_button.color("lightpink")
    play_button.penup()
    play_button.goto(0, -35)
    play_button.shapesize(stretch_wid=2, stretch_len=4)
    
    play_text = turtle.Turtle()
    play_text.speed(0)
    play_text.color("white")
    play_text.penup()
    play_text.hideturtle()
    play_text.goto(0, -50)
    play_text.write("PLAY", align="center", font=("Arial", 18, "bold"))

    # Oyun başlatma işlemi
    def start_game(x, y):
        if -50 <= x <= 50 and -70 <= y <= -30:
            play_button.hideturtle()
            play_text.clear()
            title.clear()
            game_loop()

    window.onclick(start_game)  # Ekran tıklamalarını dinle

def congratulations_screen():
    """Kutlama ekranını oluştur ve Level 2'ye geçişi tetikle."""
    window.clearscreen()  # Ekranı temizle
    window.bgcolor("#E4CBFF")
    window.title("FreakSnake")
    
    winsound.PlaySound("sounds/hit.wav",winsound.SND_ASYNC)

    # Kutlama mesajı
    congrats_message = turtle.Turtle()
    congrats_message.speed(0)
    congrats_message.color("black")
    congrats_message.penup()
    congrats_message.hideturtle()
    congrats_message.goto(0, 65)
    congrats_message.write("CONGRATULATIONS!", align="center", font=("Times New Roman", 24, "bold"))

    # Geçiş butonu
    button = turtle.Turtle()
    button.speed(0)
    button.shape("square")
    button.color("lightpink")
    button.penup()
    button.goto(0, -38)
    button.shapesize(stretch_wid=2, stretch_len=10)

    button_text = turtle.Turtle()
    button_text.speed(0)
    button_text.color("white")
    button_text.penup()
    button_text.hideturtle()
    button_text.goto(0, -50)
    button_text.write("Pass to Level 2!", align="center", font=("Arial", 18, "bold"))

    # Buton tıklama olayı
    def pass_to_level2(x, y):
        if -50 <= x <= 50 and -70 <= y <= -30:
            window.bye()  # Turtle ekranını kapat
            os.system('python freaksnakelevel2.py')  # Diğer Python dosyasını çalıştır

    # Tıklamaları dinle
    window.onclick(pass_to_level2)

def game_loop():
    # Oyun hızını belirleyen değişken
    hiz = 0.2

    # Oyun ekranını oluşturma
    window.clearscreen()
    window.bgcolor("#FFD1DF")
    window.setup(width=600, height=600)
    window.title("FreakSnake")
    window.tracer(0)

    head = turtle.Turtle()
    head.speed(0)
    head.shape('square')
    head.shape("assets/snake_head.gif")  # Yılanın kafasına bu görseli uygula
    head.penup()
    head.goto(0, 100)
    head.direction = 'stop'

    bait = turtle.Turtle()
    bait.speed(0)
    bait.shape('circle')
    bait.color('#CBA2CB')
    bait.penup()
    bait.goto(0, 0)
    bait.shapesize(0.8, 0.8)

    tails = []
    score = 0

    changebait = turtle.Turtle()
    changebait.speed(0)
    changebait.shape('square')
    changebait.color('white')
    changebait.penup()
    changebait.goto(0, 260)
    changebait.hideturtle()
    changebait.write('Score: {} / 100   Level: 1'.format(score), align='center', font=('courier', 17, 'normal'))

    def move():
        if head.direction == 'up':
            y = head.ycor()
            head.sety(y + 20)
        if head.direction == 'down':
            y = head.ycor()
            head.sety(y - 20)
        if head.direction == 'right':
            x = head.xcor()
            head.setx(x + 20)
        if head.direction == 'left':
            x = head.xcor()
            head.setx(x - 20)

    def goUp():
        if head.direction != 'down':
            head.direction = 'up'

    def goDown():
        if head.direction != 'up':
            head.direction = 'down'

    def goRight():
        if head.direction != 'left':
            head.direction = 'right'

    def goLeft():
        if head.direction != 'right':
            head.direction = 'left'

    window.listen()
    window.onkey(goUp, 'Up')
    window.onkey(goDown, 'Down')
    window.onkey(goRight, 'Right')
    window.onkey(goLeft, 'Left')

    while True:
        window.update()

        if head.xcor() > 300 or head.xcor() < -300 or head.ycor() > 300 or head.ycor() < -300:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'

            for tail in tails:
                tail.goto(1000, 1000)

            tails = []
            score = 0
            changebait.clear()
            changebait.write('Score: {} / 100   Level: 1'.format(score), align='center', font=('courier', 17, 'normal'))

        for tail in tails:
            if head.distance(tail) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = 'stop'

                for tail in tails:
                    tail.goto(1000, 1000)

                tails = []
                score = 0
                changebait.clear()
                changebait.write('Score: {} / 100   Level: 1'.format(score), align='center', font=('courier', 17, 'normal'))

        if head.distance(bait) < 20:
            
            winsound.PlaySound("sounds/eat.wav", winsound.SND_ASYNC)
            
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            bait.goto(x, y)

            hiz = max(hiz - 0.001, 0.05)

            score += 10
            changebait.clear()
            changebait.write('Score: {} / 100   Level: 1'.format(score), align='center', font=('courier', 17, 'normal'))

            newtail = turtle.Turtle()
            newtail.speed(0)
            newtail.shape('square')
            newtail.color('#CBA2CB')
            newtail.penup()
            tails.append(newtail)
        

        # Eğer skor 100 olursa, kutlama ekranını göster
        if score >= 100:
            congratulations_screen()
            break

        for i in range(len(tails) - 1, 0, -1):
            x = tails[i - 1].xcor()
            y = tails[i - 1].ycor()
            tails[i].goto(x, y)

        if len(tails) > 0:
            x = head.xcor()
            y = head.ycor()
            tails[0].goto(x, y)

        move()
        time.sleep(hiz)

# Oyun başlatma
window = turtle.Screen()
main_menu()
window.mainloop()