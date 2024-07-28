from views.view_menu import print_menu

def controller_menu(controller: function, title: str, choices: list[str]):
    while True:
        print_menu(title, choices)
        command = input('- choose: ')
        
        if command == 'exit':
            exit(0)
        elif command == 'back':
            break
        else: 
            controller()