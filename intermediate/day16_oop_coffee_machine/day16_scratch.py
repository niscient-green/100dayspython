# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
#
# my_screen = Screen()
# print(my_screen.canvheight)
# timmy.forward(100)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle"])
table.add_column("Type", ["Electric", "Water"])
print(table.align)
table.align = "l"
print(table.align)

print(table)
