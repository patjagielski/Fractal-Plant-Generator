import turtle
from collections import deque


def L_System(sentence, n):
    for i in range(n):
        next_sentence = ''
        for j in range(len(sentence)):
            character = sentence[j]
            if character == 'X':
                next_sentence += 'F+[[X]-X]-F[-FX]+X'
            elif character == 'F':
                next_sentence += 'FF'
            else:
                next_sentence += character
        print(sentence)
        sentence = next_sentence
    return sentence


def draw(sentence):
    stack = []
    window = turtle.Screen()
    # window.setup(, )
    window.bgcolor('black')
    myturtle = turtle.Turtle()
    myturtle.speed(0)
    myturtle.shape('turtle')
    myturtle.penup()
    myturtle.goto(-window.window_width()/2+window.window_height()/2, -window.window_height()/2)
    myturtle.pendown()
    myturtle.left(90)
    # myturtle.forward(50)
    # myturtle.pensize(5)

    for character in sentence:
        if character == 'F':
            myturtle.color('blue')
            myturtle.forward(5)
        elif character == '+':
            myturtle.color('green')
            myturtle.left(25)
        elif character == '-':
            myturtle.color('purple')
            myturtle.right(25)
        elif character == '[':
            myturtle.color('black')
            angle = myturtle.heading()
            pos = [myturtle.xcor(), myturtle.ycor()]
            stack.append((angle, pos))
        elif character == ']':
            myturtle.color('pink')
            angle, pos = stack.pop()
            myturtle.setheading(angle)
            myturtle.penup()
            myturtle.goto(pos[0], pos[1])
            myturtle.pendown()
        elif character == 'X':
            myturtle.color('red')
            myturtle.forward(25)
    window.exitonclick()



def init(n):
    sentence = 'X'
    instructions = L_System(sentence, n)
    draw(instructions)


n = int(input("Enter n: "))
init(n)
