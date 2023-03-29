import sys

import util
import view.ui as ui


def load_module(option):
    if option == "0":
        sys.exit()


def display_menu():
    options = ["Exit",
               "Play",
               "Option 2",
               "Option 3"]
    ui.display_menu("Roguelike", options)


def menu():
    option = None
    while option != '1':
        display_menu()
        option = util.key_pressed()
        load_module(option)