# https://docs.python.org/3/library/turtle.html
# import another_module
# print(another_module.another_variable)
#
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color('DarkOrchid2')
# timmy.fd(100)
# print(timmy.position())
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

pokemon = ['Tyranitar', 'Scizor', 'Blastoise']
pokemon_type = ['Rock-Dark', 'Bug-Steel', 'Water']


table = PrettyTable()
table.add_column('Pokemon Name', pokemon)
table.add_column('Type', pokemon_type)


table.align = 'l'

print(table)
