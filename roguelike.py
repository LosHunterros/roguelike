import util
import view.ui as ui
import controller.menu_controller as menu
import controller.level_controller as level


def main():
    menu.menu()
    level.level()
    ui.display_win()


if __name__ == "__main__":
    main()
