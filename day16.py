# import turtle
# from turtle import Turtle, Screen
# timmy = Turtle()
# turtle.title("Well Played")
# timmy.shape("turtle")
# timmy.color("white")
# timmy.forward(100)
# print(timmy)
#
# my_screen = Screen()
# my_screen.bgcolor("green")
# my_screen.exitonclick()
# print(my_screen.canvheight)

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)


