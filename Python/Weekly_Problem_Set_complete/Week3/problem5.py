import turtle


laps = int(input("How many times around the square? "))
color_mode = input("Enter a color or 'rainbow': ").lower()

t = turtle.Turtle()
t.speed(0)

side_length = 10

colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "indigo",
    "violet",
]

for side in range(laps * 4):
    if color_mode == "rainbow":
        t.color(colors[side % len(colors)])
    else:
        t.color(color_mode)

    t.forward(side_length)
    t.right(90)
    side_length += 5

turtle.done()