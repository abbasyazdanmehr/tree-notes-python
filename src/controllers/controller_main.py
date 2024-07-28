

from views.menu import print_menu
from constants import REPRESENT_APP_NAME
import choices


def controller_main(command: int):
    while True:
        print_menu(REPRESENT_APP_NAME, choices.main_menu)
        
        print("- choose: ", end='')
        command = input()

        print()

        if command == '1':
            view_all_trees()
        elif command == '2':
            new_tree()
        elif command == '3':
            exit()

    