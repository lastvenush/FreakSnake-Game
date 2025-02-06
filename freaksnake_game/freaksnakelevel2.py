import turtle
import time
import random
import os
import winsound

# Delay between steps
delay = 0.15

# Score and apple count
score = 0
apple_count = 0

# Set up the screen
wn = turtle.Screen()
wn.title("FreakSnake")
wn.bgcolor("light yellow")
wn.setup(width=600, height=600)
wn.addshape("assets/snake_head.gif")  # Görseli ekrana tanıt
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.shape("assets/snake_head.gif")  # Yılanın kafasına bu görseli uygula
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("pink")
food.penup()
food.goto(0, 100)
food.shapesize(0.8, 0.8)  # Resize the food slightly smaller

# Food 2
food2 = turtle.Turtle()
food2.speed(0)
food2.shape("circle")
food2.color("#CBA200")
food2.penup()
food2.goto(0, -100)
food2.shapesize(0.8, 0.8)  # Resize the food slightly smaller

segments = []

# Score display
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("grey")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 / 200  Level: 2", align="center", font=("courier", 17, "normal"))


# Direction functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

# Move the snake
def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

def congratulations_screen():
    """Kutlama ekranını oluştur ve Level 3'e geçişi tetikle."""
    wn.clearscreen()  # Ekranı temizle
    wn.bgcolor("#E4CBFF")
    wn.title("FreakSnake")

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
    button_text.write("Pass to Level 3!", align="center", font=("Arial", 18, "bold"))

    # Buton tıklama olayı
    def pass_to_level2(x, y):
        if -50 <= x <= 50 and -70 <= y <= -30:
            wn.bye()  # Turtle ekranını kapat
            os.system('python freaksnakelevel3.py')  # Diğer Python dosyasını çalıştır

    # Tıklamaları dinle
    wn.onclick(pass_to_level2)

# Main game loop
while True:
    wn.update()  # Update the screen

    # Collision with the screen boundary
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Reset segments
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        # Reset score
        score = 0
        apple_count = 0
        pen.clear()
        pen.write("Score: {} / 200  Level: 2".format(score), align="center", font=("courier", 17, "normal"))

    # Collision with food
    if head.distance(food) < 20:
        
        winsound.PlaySound("sounds/eat.wav", winsound.SND_ASYNC)
        
        # Move food to a random position
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("pink")
        new_segment.penup()
        segments.append(new_segment)

        # Update score
        apple_count += 1
        score = apple_count * 10

        # Display score
        pen.clear()
        pen.write("Score: {} / 200  Level: 2".format(score), align="center", font=("courier", 17, "normal"))
        
    # Collision with food 2
    if head.distance(food2) < 20:
        
        winsound.PlaySound("sounds/eat.wav", winsound.SND_ASYNC)
        
        # Move food to a random position
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food2.goto(x, y)

        # Add a new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("#CBA200")
        new_segment.penup()
        segments.append(new_segment)

        # Update score
        apple_count += 1
        score = apple_count * 10

        # Display score
        pen.clear()
        pen.write("Score: {} / 200  Level: 2".format(score), align="center", font=("courier", 17, "normal"))

    if score >= 200:
            congratulations_screen()
            break

    # Move segments
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to the head
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()  # Move the snake

    # Collision with self
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Reset segments
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            # Reset score
            score = 0
            apple_count = 0
            pen.clear()
            pen.write("Score: {} / 200  Level: 2".format(score), align="center", font=("courier", 17, "normal"))

    time.sleep(delay)  # Delay between steps
    
wn.mainloop()