

def print_menu(title: str, choices: list[str], title_board_width: int = 60):
    left_space = ((title_board_width // 2) - 1 - len(title)//2)
    right_space = (title_board_width - (2*1) - (left_space + len(title)))
    print('-' * title_board_width)
    print('|' + (' ' * left_space) + title + (' ' * right_space) + '|')
    print('-' * title_board_width)
    for i in range(len(choices)):
        print(str(i + 1), choices[i])
    