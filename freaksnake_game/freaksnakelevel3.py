import turtle
import time
import random
from turtle import Turtle
import winsound

# Delay between each frame of the game (controls game speed)
delay = 0.10

# Set up the game window
window = turtle.Screen()
window.title("FreakSnake")  # Window title
window.bgcolor("#c6d3e3")  # Background color
window.addshape("assets/snake_head.gif")  # Görseli ekrana tanıt
window.setup(width=600, height=600)  # Set dimensions of the window
window.tracer(0)  # Turns off the screen updates to allow manual refreshing

# Create the snake's head
head = turtle.Turtle()
head.speed(0)  # Fastest drawing speed
head.shape("square")  # Shape of the head
head.shape("assets/snake_head.gif")  # Yılanın kafasına bu görseli uygula
head.penup()  # Prevent the head from drawing trails
head.goto(0, 0)  # Initial position
head.direction = "stop"  # Snake starts stationary

# Create the food
food = turtle.Turtle()
food.speed(0)  # Fastest drawing speed
food.shape("circle")  # Shape of the food
food.color("#F7AA75")  # Color of the food
food.penup()  # Prevent food from drawing trails
food.goto(100, 0)  # Initial position of the food
food.shapesize(0.8, 0.8)  # Resize the food slightly smaller

# Create the food
food2 = turtle.Turtle()
food2.speed(0)  # Fastest drawing speed
food2.shape("circle")  # Shape of the food
food2.color("#F78875")  # Color of the food
food2.penup()  # Prevent food from drawing trails
food2.goto(-100, 0)  # Initial position of the food
food2.shapesize(0.8, 0.8)  # Resize the food slightly smaller

# Create the food
food3 = turtle.Turtle()
food3.speed(0)  # Fastest drawing speed
food3.shape("circle")  # Shape of the food
food3.color("#F75575")  # Color of the food
food3.penup()  # Prevent food from drawing trails
food3.goto(0, 75)  # Initial position of the food
food3.shapesize(0.8, 0.8)  # Resize the food slightly smaller

# Initialize the snake's body and the score
tails = []  # List to hold the snake's body segments
score = 0  # Player's score

# Display the score and level
text = turtle.Turtle()
text.speed(0)  # Fastest drawing speed
text.shape("square")
text.color("white")
text.penup()  # Prevent drawing
text.goto(0, 260)  # Position for the score display
text.hideturtle()  # Hide the turtle cursor
# Initial text display
text.write("Score: {}/300   Level: 3".format(score), align="center", font=("courier", 17, "normal"))

# Define movement logic
def move():
    # Move up
    if head.direction == "up":
        y = head.ycor()  # Get the current y-coordinate
        head.sety(y + 20)  # Move up by 20 units
    # Move down
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    # Move right
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    # Move left
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

# Direction control functions (prevent snake from reversing direction)
def goUp():
    if head.direction != "down":
        head.direction = "up"

def goDown():
    if head.direction != "up":
        head.direction = "down"

def goRight():
    if head.direction != "left":
        head.direction = "right"

def goLeft():
    if head.direction != "right":
        head.direction = "left"

# Listen for keyboard input
window.listen()
window.onkey(goUp, "Up")  # Move up
window.onkey(goDown, "Down")  # Move down
window.onkey(goRight, "Right")  # Move right
window.onkey(goLeft, "Left")  # Move left

def congratulations_screen():
    """Kutlama ekranını oluştur ve Oyunu Bitir."""
    window.clearscreen()  # Ekranı temizle
    window.bgcolor("#E4CBFF")
    window.title("FreakSnake")
    window.setup(width=1000, height=600)
    
    winsound.PlaySound("sounds/hit.wav",winsound.SND_ASYNC)

    # Kutlama mesajı
    congrats_message = turtle.Turtle()
    congrats_message.speed(0)
    congrats_message.color("black")
    congrats_message.penup()
    congrats_message.hideturtle()
    congrats_message.goto(0, 0)
    congrats_message.write("CONGRATULATIONS, YOU FINISHED THE GAME!!!", align="center", font=("Arial", 25, "bold"))
    
    # Pencereyi açık tut
    time.sleep(5)  # 5 saniye bekle (isteğe bağlı)
    window.bye()  # Oyunu kapat veya `window.exitonclick()` kullan

# Main game loop
while True:
    window.update()  # Refresh the screen

    # Check for collision with the walls
    if head.xcor() > 300 or head.xcor() < -300 or head.ycor() > 300 or head.ycor() < -300:
        time.sleep(1)  # Pause before resetting
        head.goto(0, 0)  # Reset head to the center
        head.direction = "stop"  # Stop the snake

        # Move all tails off-screen
        for tail in tails:
            tail.goto(1000, 1000)  # Send tail segments far off-screen

        tails = []  # Clear the tail list
        score = 0  # Reset the score
        text.clear()  # Clear the old text
        text.write("Score: {}/300   Level: 3".format(score), align="center", font=("courier", 17, "normal"))
        
    for tail in tails:
            if head.distance(tail) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = 'stop'

                for tail in tails:
                    tail.goto(1000, 1000)

                tails = []
                score = 0
                text.clear()
                text.write('Score: {} / 300   Level: 3'.format(score), align='center', font=('courier', 17, 'normal'))

    # Check for collision with food
    if head.distance(food) < 20:  # If the head is close enough to the food
        
        winsound.PlaySound("sounds/eat.wav", winsound.SND_ASYNC)
        
        # Move the food to a random location
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        food.goto(x, y)

        # Increase the score
        score += 10
        text.clear()  # Update the score display
        text.write("Score: {}/300   Level: 3".format(score), align="center", font=("courier", 17, "normal"))

        # Add a new tail segment
        newTail = turtle.Turtle()
        newTail.speed(0)
        newTail.shape("square")
        newTail.color("#F7AA75")
        newTail.penup()
        tails.append(newTail)
        
    # Check for collision with food
    if head.distance(food2) < 20:  # If the head is close enough to the food
        
        winsound.PlaySound("sounds/eat.wav", winsound.SND_ASYNC)
        
        # Move the food to a random location
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        food2.goto(x, y)

        # Increase the score
        score += 10
        text.clear()  # Update the score display
        text.write("Score: {}/300   Level: 3".format(score), align="center", font=("courier", 17, "normal"))

        # Add a new tail segment
        newTail = turtle.Turtle()
        newTail.speed(0)
        newTail.shape("square")
        newTail.color("#F78875")
        newTail.penup()
        tails.append(newTail)
    
    # Check for collision with food
    if head.distance(food3) < 20:  # If the head is close enough to the food
        
        winsound.PlaySound("sounds/eat.wav", winsound.SND_ASYNC)
        
        # Move the food to a random location
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        food3.goto(x, y)

        # Increase the score
        score += 10
        text.clear()  # Update the score display
        text.write("Score: {}/300   Level: 3".format(score), align="center", font=("courier", 17, "normal"))

        # Add a new tail segment
        newTail = turtle.Turtle()
        newTail.speed(0)
        newTail.shape("square")
        newTail.color("#F75575")
        newTail.penup()
        tails.append(newTail)    

    if score >= 300:
            congratulations_screen()
            break

    # Move the tail segments in reverse order
    for i in range(len(tails) - 1, 0, -1):
        x = tails[i - 1].xcor()  # Get the x-coordinate of the previous segment
        y = tails[i - 1].ycor()  # Get the y-coordinate of the previous segment
        tails[i].goto(x, y)  # Move the current segment to the position of the previous segment

    # Move the first tail segment to follow the head
    if len(tails) > 0:
        x = head.xcor()
        y = head.ycor()
        tails[0].goto(x, y)

    move()  # Move the snake's head

    time.sleep(delay)  # Pause for a short time