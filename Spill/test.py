import turtle
import random

# Setup screen
screen = turtle.Screen()
screen.title("Ghost Game")
screen.setup(width=600, height=400)
screen.bgcolor("white")

# Create turtle for drawing
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()

# Function to draw doors
def draw_doors(selected_door, ghost_door):
    pen.clear()
    pen.goto(-150, 0)
    for door in range(3):
        if door + 1 == selected_door:
            pen.color("black")
            pen.begin_fill()
        elif door + 1 == ghost_door:
            pen.color("red")
            pen.begin_fill()
        else:
            pen.color("green")
            pen.begin_fill()

        for _ in range(2):
            pen.forward(100)
            pen.left(90)
            pen.forward(150)
            pen.left(90)

        pen.end_fill()
        pen.forward(150)

# Game logic
def ghost_game():
    print('Ghost Game')
    score = 0
    while True:
        ghost_door = random.randint(1, 3)
        print('Three doors ahead...')
        door = int(screen.textinput('Ghost Game', 'Which door do you open? (1, 2, or 3): '))
        if door == ghost_door:
            print('GHOST')
            draw_doors(door, ghost_door)
            break
        elif door < 1 or door > 3:
            print('Invalid choice, please choose again :)')
        else:
            print('No ghost!')
            print('You enter the next room.')
            score += 1
            draw_doors(door, ghost_door)

    print('Run away!')
    print('Game Over! You scored', score)

# Main function
def main():
    ghost_game()
    screen.mainloop()

if __name__ == "__main__":
    main()